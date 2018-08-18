def centered_average(nums):
  s = 0
  for i in range(len(nums)):
    s += nums[i]
  
  x = (s - min(nums) - max(nums)) / (len(nums) -2)
  return x
