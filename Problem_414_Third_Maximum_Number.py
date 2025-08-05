class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=set(nums)
        nums=list(a)
        nums.sort()
        nums.reverse()
        if len(nums)>=3:
            return nums[2]
        else:
            return nums[0]