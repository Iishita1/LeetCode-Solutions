
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        str1=''
        rev1 = []
        n1 = l1
        while n1 is not None:
            rev1.append(n1.val)
            n1 = n1.next
        l1n=rev1[::-1]
        for i in l1n:
            s1=str(i)
            str1=str1+s1
        str2 = ''
        rev2 = []
        n2 = l2
        while n2 is not None:
            rev2.append(n2.val)
            n2 = n2.next
        l2n=rev2[::-1]
        for j in l2n:
            s2=str(j)
            str2=str2+s2
        int1=int(str1)
        int2=int(str2)
        int3=int1+int2
        str3=str(int3)
        rev3=[]
        for k in str3:
            rev3.append(k)
        l3n = rev3[::-1]
        l3=ListNode(int(l3n[0]))
        tail=l3
        e = 1
        while e < len(l3n):
            z=int(l3n[e])
            tail.next = ListNode(z)
            tail = tail.next
            e+=1
        return l3 