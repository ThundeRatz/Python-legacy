# Python-legacy
Legacy Python code.

----------------------------------------------------------------------

##About
Code used in our first competition with the ThunderWaze robot, Winter Challenge 2014.
This code is no longer mantained (we moved to C/C++) and won't be translated.
Many functions have been enhanced in recent versions, using this branch isn't recommended.

##Features
This branch has most of the code used in 2014. It uses:

- A serial USB GPS
- HMC5883L compass
- Our motor controlling board

Also included is a Python server using [tornado](http://www.tornadoweb.org/) displaying information on GPS, compass and battery voltage and allowing basic configuration of GPS coordinates.
This was an interesting feature that was dropped in later versions.

We used a USB Webcam, too, but image processing code isn't included. It was done based on color blobs.
The code in this repository should be enough to start development of a robot.

##Lost?
https://github.com/ThundeRatz/trekking-magellan-docs

##Licence
[<img src="https://i.creativecommons.org/l/by/4.0/88x31.png">](http://creativecommons.org/licenses/by/4.0/)

Except where otherwise noted, ThunderTrekking by [ThundeRatz](http://www.thunderatz.org) is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
