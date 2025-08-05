class Solution:
    def fib(self, n: int) -> int:
        a=0 
        b=1
        for i in range(0,n):
            temp=b
            b=a+b
            a=temp
        return a