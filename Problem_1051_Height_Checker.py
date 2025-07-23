class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights1=heights.copy()
        heights.sort()
        d=0
        for i in range(0,len(heights)):
            if heights[i]!=heights1[i]:
                d+=1
        return d