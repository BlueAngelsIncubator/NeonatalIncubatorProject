from random import randint
import board, busio
from adafruit_tmp006 import TMP006
import time

class PatientSensors():
  tempSensor   = None
  o2Sensor     = None
  weightSensor = None
  t0           = None
  t1           = None
  o2   = 94
  w    = 2.6
  hr   = 140

  def __init__(self):
    self.tempSensor = TMP006(busio.I2C(board.SCL, board.SDA))
    self.t0 = time.time()
    self.t1 = time.time()

  def temperature(self):
    return self.tempSensor.temperature

  def o2sat(self):
    t = time.time()

    if self.t0 is None:
      self.t0 = t
      return self.o2
    elif ((t-self.t0) > 4):
        self.t0 = t
        self.o2 = self.o2 + randint(-1, 1)
        if self.o2 > 100:
            self.o2=98
        return self.o2
    else:
      return self.o2

  def weight(self):
    return self.w

  def heart_rate(self):
    t = time.time()

    if self.t1 is None:
      self.t1 = t
      return self.hr
    elif ((t-self.t1) > 3):
        self.t1 = t
        self.hr = self.hr + randint(-2, 2)
        return self.hr
    else:
      return self.hr
