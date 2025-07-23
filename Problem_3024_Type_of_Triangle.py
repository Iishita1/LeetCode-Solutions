class Solution:
    def triangleType(self, nums: List[int]) -> str:
        return ('none','equilateral','isosceles','scalene')[(max(a)<min(a)+median(a))*len({*a})]