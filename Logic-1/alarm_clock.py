def alarm_clock(day, vacation):
  if not vacation:
    if 0 < day < 6:
      return "7:00"
    else:
      return "10:00"
  else:
    if 0 < day < 6:
      return "10:00"
      
  return "off"
