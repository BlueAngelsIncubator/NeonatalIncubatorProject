from tkinter import *
from AmbientReadings import EnvironmentSensors

class environment:
  root    = None
  temp    = None
  tLabel  = None
  rh      = None
  rhLabel = None
  color   = None
  bg      = None
  sensors = None

  def __init__(self, masterScreen, color='green', bg='black'):
    self.color = color
    self.bg    = bg

    self.root = LabelFrame( masterScreen,                        # init master frame
                            text='  Ambient',
                            bd=0, font=('fixed', 32),
                            bg=self.bg, fg=self.color,
                            highlightbackground=self.color, 
                            highlightcolor=self.color,
                            highlightthickness=8,
                            padx=0, pady=20
                          )
    self.root.pack()                                      # pack and place on screen
    self.root.place(x=16, y=252, height=212, width=376)

    # init frame labels
    self.temp = Label(self.root, font=('fixed', 24))
    self.rh   = Label(self.root, font=('fixed', 24))

    self.tLabel = Label( self.root,
                         text='Temperature:', 
                         fg=self.color,
                         bd=0, bg=self.bg,
                         font=('fixed', 14),
                         padx=0, pady=0
                       )
    
    self.rhLabel = Label( self.root,
                          text='Humidity:', 
                          fg=self.color,
                          bd=0, bg=self.bg,
                          font=('fixed', 14),
                          padx=0, pady=0
                        )

    # pack and place on screen
    self.temp.pack()
    self.temp.place(x=160, y=0)
    self.rh.pack()
    self.rh.place(x=172, y=45)

    self.tLabel.pack()
    self.tLabel.place(x=24,y=0)
    self.rhLabel.pack()
    self.rhLabel.place(x=24,y=45)

    self.sensors = EnvironmentSensors()

  def update(self):
    self.temp.config( text='{0:.01f} °C'.format(self.sensors.temperature()),
                      fg=self.color,
                      bg=self.bg
                    )
                    
    self.rh.config( text='{0:.01f}%'.format(self.sensors.humidity()),
                    fg=self.color,
                    bg=self.bg
                  )