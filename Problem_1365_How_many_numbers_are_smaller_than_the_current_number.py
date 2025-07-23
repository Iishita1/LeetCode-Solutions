class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in range(0,len(nums)):
            a=0
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    a+=1
            l1.append(a)
        return l1