from tkinter import *
from Patient import infant
from Ambient import environment
from Machine import incubator
from pytz import timezone
import glob, time, datetime

class Monitor:
  root         = None
  clock        = None
  patientStats = None
  ambientStats = None
  machineStats = None
  normalColor  = 'white'
  bgColor      = 'black'
  tz           = 'US/Eastern'
  currentTime  = None
  prevTime     = None

  def __init__(self):
    self.init_root()
    self.init_compartments()
    self.init_clock()
  
  def init_root(self):
    self.root = Tk()
    self.root.title('Incubator')
    self.root.configure(bg='black')
    self.root.geometry('800x480')

  def init_clock(self):
    self.clock = Label(self.root, font=('fixed', 12))
    self.clock.place(x=616, y=8)              # Clock's Relative Position on Monitor

  def init_compartments(self):
    self.patientStats = infant(self.root, self.normalColor, self.bgColor)
    self.ambientStats = environment(self.root, self.normalColor, self.bgColor)
    self.machineStats = incubator(self.root, self.normalColor, self.bgColor)

  def update(self):
    self.currentTime = datetime.datetime.now(timezone(self.tz))
    
    if self.currentTime != self.prevTime:
      self.prevTime = self.currentTime
      
      self.clock.config( text=self.currentTime.strftime('%d-%b-%Y %I:%M %p'),
                         fg='white',
                         bg=self.bgColor
                       )

    self.patientStats.update()
    self.ambientStats.update()
    self.machineStats.update()
    
    self.clock.after(100, self.update)

if __name__=='__main__':
  vm = Monitor()
  vm.update()

  vm.root.mainloop()
