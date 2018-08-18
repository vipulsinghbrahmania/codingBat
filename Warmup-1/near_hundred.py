def near_hundred(n):
  x = 100 - n
  y = 200 - n
  if abs(x) <= 10 or abs(y) <= 10:
    return True
  else:
    return False
