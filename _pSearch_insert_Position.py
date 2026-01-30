class Solution(object):
  def containsDuplicate(slef, nums):
    nums= sorted(nums)
    for i in range(len(nums)-1_:
      if nums[i] == nums[i+1]:
        return True
    return False
