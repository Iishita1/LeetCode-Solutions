class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while x>0:
            y=2*i-1
            x=x-y
            i+=1
        if x<0: 
            return i-2
        else:
            return i-1
                    

            