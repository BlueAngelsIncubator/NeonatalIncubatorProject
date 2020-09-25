from tkinter import *
import MachineReadings as status

class incubator:
  root     = None
  ac_pwr   = None
  warnings = None
  color    = None
  bg       = None

  def __init__(self, masterScreen, color='purple', bg='black'):
    self.color = color
    self.bg    = bg

    self.root = LabelFrame( masterScreen,                        # init master frame
                            text=' Status',
                            bd=0, font=('fixed', 32),
                            bg='black', fg=self.color,
                            highlightbackground=self.color,
                            highlightcolor=self.color,
                            highlightthickness=8,
                            padx=2.5, pady=2.5
                          )
    self.root.pack()                                      # pack and place on screen
    self.root.place(x=408, y=252, height=212, width=376)

    # init frame labels
    self.ac_pwr  = Label(self.root, font=('fixed', 24))
    self.alarm_status = Label(self.root, font=('fixed', 24))
    self.warnings = LabelFrame( self.root, 
                                padx=10, pady=10,
                                bd=0, font=('fixed', 24)
                              )

    self.temp = Label(self.warnings, font=('fixed', 24))
    self.humidity = Label(self.warnings, font=('fixed', 24))
    self.apnea = Label(self.warnings, font=('fixed', 24))
    self.hr = Label(self.warnings, font=('fixed', 26))
    self.o2 =  Label(self.warnings, font=('fixed', 24))


    # pack and place on screen
    self.ac_pwr.pack()
    self.warnings.pack(fill='x')

    self.temp.pack(side=LEFT)
    self.humidity.pack()
    self.humidity.place(relx=0.25, rely=0)
    self.apnea.pack()
    self.apnea.place(relx=0.45, rely=0)
    self.hr.pack()
    self.hr.place(relx=0.65, rely=0.025)
    self.o2.pack(side=RIGHT)

  def update(self):                    # init all sensor readings at each clock tick
    warnings = status.check_alarms()

    self.ac_pwr.config( text='Power: {}'.format(status.AC_power_state()),
                        fg=self.color,
                        bg=self.bg
                      )

    self.warnings.config( text='    Alarm Status: {}'.format(status.alarm_state()),
                          fg=self.color,
                          bg=self.bg
                        )
    
    self.temp.config( text=' ',
                      fg=warnings[0],
                      bg=self.bg
                    )

    self.humidity.config( text='',
                          fg=warnings[1],
                          bg=self.bg
                        )
    
    self.apnea.config( text='A',
                       fg=warnings[2],
                       bg=self.bg
                     )

    self.hr.config( text='',
                    fg=warnings[3],
                    bg=self.bg
                  )

    self.o2.config( text='O₂ ',
                    fg=warnings[4],
                    bg=self.bg
                  )



# Icons:
#      
#  
