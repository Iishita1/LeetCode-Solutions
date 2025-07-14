class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=list(filter(None,s.split(" ")))
        return len(k[len(k)-1])
