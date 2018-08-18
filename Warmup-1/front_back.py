def front_back(str):
  if len(str) == 1:
    return str
  else:
    f = str[:1]
    l = str[len(str)-1 : len(str)]
    mid = str[1 : len(str)-1]
    return l+mid+f
