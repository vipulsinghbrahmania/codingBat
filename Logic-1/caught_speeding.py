def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5
    
  if speed <= 60:
    return 0
  elif 60 < speed <= 80:
    return 1
  
  return 2
