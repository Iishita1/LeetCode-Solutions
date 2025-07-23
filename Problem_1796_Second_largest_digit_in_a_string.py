class Solution:
    def secondHighest(self, s: str) -> int:
        p = set()
        for i in s:
            if '0' <= i <= '9':
                p.add(int(i))
        if len(p) > 1:
            p.remove(max(p))
            return max(p)
        return -1
