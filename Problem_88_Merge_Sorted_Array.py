class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l3=[]
        for i in range(0,m):
            l3.insert(i,nums1[i])
        for j in range(0,n):
            l3.append(nums2[j])
        l3.sort()
        for k in range(0,m+n):
            nums1[k]=l3[k]
        
        