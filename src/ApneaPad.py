#!/bin/python3

import board, busio, time
import adafruit_ads1x15.ads1015 as ADC
from adafruit_ads1x15.analog_in import AnalogIn
from threading import Thread
from numpy import diff

class ApneaPad():
  ApneaMonitor = None
  adcChannel   = None
  rdg_buffer   = None

  def __init__(self):
    i2c_bus = busio.I2C(board.SCL, board.SDA)
    adc     = ADC.ADS1015(i2c_bus)
    self.adc_channel_0 = AnalogIn(adc, ADC.P0)
    self.rdg_buffer    = []

    # Spawn ApneaMonitor Thread
    self.ApneaMonitor = Thread(
                                target = self.update_buffer,
                                name   = 'ApneaMontor',
                              )
    self.ApneaMonitor.daemon = True
    self.ApneaMonitor.start()

  
  def update_buffer(self):
    while True:
      if len(self.rdg_buffer) is 80:
        self.rdg_buffer = self.rdg_buffer[1:79]
      self.rdg_buffer.append(self.adc_channel_0.voltage)
      time.sleep(0.25)

  def check_apnea(self):
    if len(self.rdg_buffer) >= 5:
      dBreathRate = diff(self.rdg_buffer)
      if any(delta > 0.09 for delta in dBreathRate):
        return True
      else:
        return False
    else:
      return False

  def run(self):
    print('Running Apnea Monitor')
    
    try:
      while True:
        print(self.check_apnea())
        time.sleep(1)
    except KeyboardInterrupt:
      print('Done')
  
if __name__ == '__main__':
  ApneaPad = ApneaPad()
  ApneaPad.run()