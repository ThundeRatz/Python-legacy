from gps import *
import time
import threading
import math
import gira_angulo
import angulo_desejado
from motors import *
from hmc5883l import getHeading

class GpsController(threading.Thread):
	"""Thread que rodara fazendo polling dos dados do GPS"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.running = False
   
    def run(self):
        self.running = True
        while self.running:
            # grab EACH set of gpsd info to clear the buffer
            self.gpsd.next()

    def stopController(self):
        self.running = False
 
    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc

    @property
    def satellites(self):
        return self.gpsd.satellites

if __name__ == '__main__':
    # create the controller
    gpsc = GpsController() 
    try:
        # start controller
        gpsc.start()
        while True:
            print "latitude ", gpsc.fix.latitude
            print "longitude ", gpsc.fix.longitude
            print "time utc ", gpsc.utc, " + ", gpsc.fix.time
            print "altitude (m)", gpsc.fix.altitude
            print "eps ", gpsc.fix.eps
            print "epx ", gpsc.fix.epx
            print "epv ", gpsc.fix.epv
            print "ept ", gpsc.gpsd.fix.ept
            print "speed (m/s) ", gpsc.fix.speed
            print "climb ", gpsc.fix.climb
            print "track ", gpsc.fix.track
            print "mode ", gpsc.fix.mode
            print "sats ", gpsc.satellites
            time.sleep(0.5)

    #Error
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

    #Ctrl C
    except KeyboardInterrupt:
        print "User cancelled"

    finally:
        print "Stopping gps controller"
        gpsc.stopController()
        #wait for the tread to finish
        gpsc.join()
     
    print "Done"
distancia_desejada = 5 #distancia do overlap com o alvo, em metros
tol_angulo = 10 #tolerancia do angulo, em graus
alvo = [latitude, longitude] #coordenadas do alvo (devem ser inputadas manualmente)
motors = Motores()
while not (-(distancia_desejada)**2<(((gpsc.fix.latitude-alvo[0])*(1/111111))**2)+(((gpsc.fix.longitude-alvo[1])*(1/111111))**2)<(distancia_desejada)**2):
	"""Enquanto nao estivermos na distancia de overlap com o alvo (circulo de raio ajustavel centrado no alvo)"""
	motors.setSpeed(100, 100)
	if not -tol_angulo<getHeading()-angulo_desejado(alvo, [gpsc.fix.latitude, gps.fix.longitude])<tol_angulo:
		"""Se estivermos fora da faixa de tolerancia do angulo da trajetoria"""
		motors.setSpeed(0, 0)#Paramos o robo, e em seguida giramos para o angulo desejado
		gira_angulo(angulo_desejado(alvo, [gpsc.fix.latitude, gps.fix.longitude]))
motor.setSpeed(0, 0)
