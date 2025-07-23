class Solution:
    def scoreOfString(self, s: str) -> int:
        l1=[]
        for i in s:
            l1.append(ord(i))
        a,b=0,0
        for j in range(1,len(l1)):
            a=abs(l1[j-1]-l1[j])
            b+=a
        return b