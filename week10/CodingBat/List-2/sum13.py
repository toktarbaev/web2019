def sum13(nums):
  if not nums:
    return 0
  sum = 0
  if nums[0] != 13:
    sum += nums[0]
  for i in range(1, len(nums)):
    if nums[i] != 13 and nums[i - 1] != 13:
      sum += nums[i]
  return sum