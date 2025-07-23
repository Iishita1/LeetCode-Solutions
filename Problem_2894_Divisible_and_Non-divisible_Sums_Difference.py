class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s=0
        for i in range(0,n+1):
            if i%m!=0:
                s+=i
        y=0
        for i in range(0,n+1):
            if i%m==0:
                y+=i
        return s-y
        