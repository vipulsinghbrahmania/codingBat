def sum67(nums):
  f = False
  s = 0
  if len(nums) == 0:
    return 0
  else:
    for i in range(len(nums)):
      if nums[i] == 6 and not f:
        f = True
      elif nums[i] == 7 and f:
        f = False
        
      elif not f:
        s += nums[i]
        
  return 
