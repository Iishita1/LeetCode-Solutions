class Solution:
    def divisorGame(self, n: int) -> bool:
        l1=[]
        for i in range(0,n):
            l1.append(i)
        if len(l1)%2==0:
            return True
        else:
            return False