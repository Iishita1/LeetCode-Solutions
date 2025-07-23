class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            l1=list(map(int,str(i)))
            if len(l1)%2==0:
                k+=1
        return k
