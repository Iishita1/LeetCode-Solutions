class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        h = max(nums)
        for i in nums:
            if i != h and h < 2 * i:
                return -1
        return nums.index(h)