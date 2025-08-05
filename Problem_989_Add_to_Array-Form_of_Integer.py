class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(0) 
        a=""
        for i in num:
            a+=str(i)
        s=int(a)+k
        l=[]
        for i in str(s):
            l.append(int(i))
        return l