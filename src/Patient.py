from tkinter import *
from PIL import Image, ImageTk
from PatientReadings import PatientSensors

class infant:
  root       = None
  stats      = None
  hr_frame   = None
  bpm        = None
  temp       = None
  o2sat      = None
  weight     = None
  heart_rate = None
  color      = None
  tLabel     = None
  o2Label    = None
  wLabel     = None
  bg         = None
  sensors    = None

  def __init__(self, masterScreen, color='blue', bg='black'):
    img = ImageTk.PhotoImage(                                       # load hr image
                              Image.open('/home/pi/VitalsMonitor/heart.png')
                            )
    self.color = color
    self.bg    = bg

    self.root = LabelFrame( masterScreen,                       # init master frame
                            text='  Patient',
                            bd=0, font=('fixed', 32),
                            bg=self.bg, fg=self.color,
                            highlightbackground=self.color,
                            highlightcolor=self.color, 
                            highlightthickness=8,
                            padx=0, pady=0
                          )
    self.root.pack()                                      # pack and place on screen
    self.root.place(x=16, y=16, height=220, width=768)

    self.stats = LabelFrame( self.root,                           # init stats frame
                             bd=0, bg=self.bg,
                             padx=10, pady=0
                            )
    self.stats.pack()                                     # pack and place on screen
    self.stats.place(x=64, y=0, height=150, width=325)

    self.hr_frame = Label( self.root,                         # init master hr frame
                           bd=0, bg=self.bg,
                           padx=0, pady=0,
                           image=img
                         )
    self.hr_frame.image = img                                 # set background image
    self.hr_frame.pack()                                  # pack and place on screen
    self.hr_frame.place(relx=0.5, rely=-0.25, height=150, width=350)

    # init frame labels
    self.temp   = Label(self.stats, font=('fixed', 24))
    self.o2sat  = Label(self.stats, font=('fixed', 24))
    self.weight = Label(self.stats, font=('fixed', 24))

    self.heart_rate = Label(self.hr_frame, font=('fixed', 24))
    self.bpm = Label( self.hr_frame,
                      text='bpm', fg=self.color,
                      bd=0, bg=self.bg,
                      font=('fixed', 12),
                      padx=0, pady=0
                    )

    # pack and place on screen
    self.temp.pack()
    self.o2sat.pack()
    self.weight.pack()

    self.heart_rate.pack()
    self.heart_rate.place(relx=0.4, rely=0.32)

    self.bpm.pack()
    self.bpm.place(relx=0.422, rely=0.58, height=23, width=50)

    self.tLabel = Label( self.root,
                         text='Temperature:', 
                         fg=self.color,
                         bd=0, bg=self.bg,
                         font=('fixed', 14),
                         padx=0, pady=0
                       )
    
    self.o2Label = Label( self.root,
                          text='O₂ Saturation:', 
                          fg=self.color,
                          bd=0, bg=self.bg,
                          font=('fixed', 14),
                          padx=0, pady=0
                        )
    
    self.wLabel = Label( self.root,
                         text='Weight:', 
                         fg=self.color,
                         bd=0, bg=self.bg,
                         font=('fixed', 12),
                         padx=0, pady=0
                       )
    
    self.tLabel.pack()
    self.tLabel.place(x=20,y=0)
    self.o2Label.pack()
    self.o2Label.place(x=20,y=45)
    self.wLabel.pack()
    self.wLabel.place(x=20,y=90)

    self.sensors = PatientSensors()

  def update(self):
    self.temp.config( text='{0:.01f} °C'.format(self.sensors.temperature()),
                      fg=self.color,
                      bg=self.bg
                    )

    self.o2sat.config( text='{0:02d}%'.format(self.sensors.o2sat()),
                       fg=self.color,
                       bg=self.bg
                     )
                     
    self.weight.config( text='{} kg'.format(self.sensors.weight()),
                        fg=self.color,
                        bg=self.bg
                      )

    self.heart_rate.config( text='{0:03d}'.format(self.sensors.heart_rate()),
                            fg=self.color,
                            bg=self.bg
                          )
