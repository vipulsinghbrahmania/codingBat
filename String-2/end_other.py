def end_other(a, b):
  s, m = a, b
  if len(b) < len(a):
    s, m = b, a
  
  x = m[-len(s):]
  if x.lower() == s.lower():
    return True
  
  return False
