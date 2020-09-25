from random import randint
from adafruit_dht import DHT22
import board, OneWire
import time

class EnvironmentSensors():
  tempSensor = None
  rhSensor   = None
  rh         = 0

  def __init__(self):
    self.tempSensor = OneWire.TempSensor()
    self.rhSensor   = DHT22(board.D16)

  def temperature(self):
    return self.tempSensor.tempC()

  def humidity(self):
    try:  # sensor occasionally raises a checksum error
      reading = self.rhSensor.humidity
      if reading <= 100: # sensor occasionally reads 3303.2% rh
        self.rh = reading
    except RuntimeError as e:
      pass  # return previous reading, will update next tick
    
    return self.rh
