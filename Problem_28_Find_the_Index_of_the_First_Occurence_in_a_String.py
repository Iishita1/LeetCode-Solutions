class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        len_hay = len(haystack)
        len_needle = len(needle)
        if len_hay < len_needle:
            return -1
        for i in range(len_hay - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1
        