def string_match(a, b):
  small = min(len(a), len(b))
  c = 0
  
  for i in range(small-1):
    a_x = a[i:i+2]
    b_x = b[i:i+2]
    if a_x == b_x:
      c += 1
      
  return c
