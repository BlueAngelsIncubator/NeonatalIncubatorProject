# Raspberry Pi Vitals Monitor
This repository contains code for an Open Source Vitals Monitor based on a Raspberry Pi Single Board Computer.  This monitor is specifically designed for use with an open source infant incubator *(link here when ready).* The project was 

**NOTE:** This project is still under development, and is **NOT** ready for use.

###### documentation incomplete
---
#### Dependencies:
Below are the dependencies for this project, including both the APT packages as well as the pip modules. These also be found in apt_requirements.txt and pip_requirements.txt respectively. Automated installation of these modules will be included in an initialization script.

**apt packages:**
 - python3
 - python3-tk
 - wmctrl


**pip modules:**
- PIL
- pytz
- pyserial
- adafruit-circtuitpython-lis3dh
- adafruit-circuitpython-tmp006
- adafruit-circuitpython-dht
- adafruit-circuitpython-ads1x15

### How to Run:
After connecting all sensors and monitor to the Raspberry Pi, the VitalsMonitor can be run with the following command: `python3 Monitor.py`
###### note: The Pi can be configured to run this command (and any other necessary set up) automatically upon startup. (instructions for this to be added)

### Code Outline:
- Monitor.py : 'Main()', this is the only script that should be run directly (see above).
	- OneWire.py: drivers for OneWire devices
	- Patient.py: Initializes frame for patient information and updates readings.
	- Ambient.py: Initializes frame for ambient information and updates readings.
	- Machine.py: Initializes frame for machine status and updates readings.
	- Sensors.py: Sensor Drivers

## Current Status:
Currently, this project contains completed code for reading and reporting the following sensors:
- Patient:
	- Temperature
	- ~~Oxygen Saturation~~
	- ~~Weight~~
	- Apnea
	- Heart Rate
- Ambient:
	- Temperature
	- Humidity
- Machine Status:
	- ~~Power Status~~
	- Alarm Status
	- Warning Symbols
	
## Schematic:
![Vitals Monitor Schematic](docs/VitalsMonitorSchematic.png)
