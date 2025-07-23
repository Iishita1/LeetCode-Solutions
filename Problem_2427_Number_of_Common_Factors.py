class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        s1=set()
        s2=set()
        for i in range(1,a+1):
            if a%i==0:
                s1.add(i)
        for j in range(1,b+1):
            if b%j==0:
                s2.add(j)
        s3=s1.intersection(s2)
        return len(s3)