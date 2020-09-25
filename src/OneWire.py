import time, glob

class TempSensor:
  sensorFile = None

  def __init__(self):
    oneWireDir = '/sys/bus/w1/devices/'
    sensorDir = glob.glob(oneWireDir + '28*')[0]    # First device on One-Wire bus
    self.sensorFile = sensorDir + '/w1_slave'

  def rawTemp(self):
    with open(self.sensorFile, 'r') as sensor:
      l = sensor.readlines()
    return l

  def tempC(self):
    raw = self.rawTemp()
    while raw[0].strip()[-3:] != 'YES':
      time.sleep(0.1)
      raw = self.rawTemp()
    
    idx = raw[1].find('t=')
    if idx != -1:
      tStr = raw[1][idx+2:]
      celsius = float(tStr)/1000.0
      
      return celsius