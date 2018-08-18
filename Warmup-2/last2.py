def last2(str):
  if len(str) < 2:
    return 0
    
  last = str[len(str)-2:]
  c = 0
  
  for i in range(len(str)-2):
    x = str[i:i+2]
    if x == last:
      c += 1
      
  return c
