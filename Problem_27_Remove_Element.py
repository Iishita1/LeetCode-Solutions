class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=[]
        for i in nums:
            if val != i:
                k.append(i)
        nums.clear()
        for j in k:
            nums.append(j)