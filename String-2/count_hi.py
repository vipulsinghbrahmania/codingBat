def count_hi(str):
  c = 0
  for i in range(len(str)-1):
    x = str[i:i+2]
    if x == "hi":
      c += 1
      
  return c
