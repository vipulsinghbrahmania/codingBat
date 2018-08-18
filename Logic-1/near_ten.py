def near_ten(num):
  x = num % 10
  if x <= 2 or x == 8 or x == 9:
    return True
  return False
