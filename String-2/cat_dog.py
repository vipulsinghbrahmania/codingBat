def cat_dog(str):
  cat, dog = 0, 0
  for i in range(len(str)-2):
    x = str[i:i+3]
    if x == "cat":
      cat += 1
    elif x == "dog":
      dog += 1
      
  if cat == dog:
    return True
  
  return False

