import statistics
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        k=statistics.multimode(nums)
        p=0
        for i in k:
            for j in nums:
                if i==j:
                    p+=1
        return p