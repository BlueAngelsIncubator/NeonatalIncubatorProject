def AC_power_state():
  connected = True
  if connected:
     return ''
  else:
    return ''

def alarm_state():
  alarms = True # Button to mute alarms
  
  if alarms:
    a = ''
  return '{}'.format(a)
  
def check_alarms():
  warnings = [
                False,  # T
                False,  # RH
                False,  # A
                False,  # HR
                False   # O2
             ]
  colors = [ get_color(w) for w in warnings]
  return colors

def get_color(alarm):
  if alarm:
    return 'red'
  else:
    return 'dark slate grey'
