def has22(nums):
  for i in range(0, len(nums)-1):
    if nums[i:i+2] == [2,2]:
      return True    
  return False