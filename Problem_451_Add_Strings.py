class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(0) 
        n1=""
        for i in num1:
            n1+=i
        n2=""
        for i in num2:
            n2+=i
        r=int(n1)+int(n2)
        return str(r)