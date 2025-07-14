class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        used_chars = {}
        longest_sub = ""

        for i, char in enumerate(s):
            if char in used_chars and used_chars[char] >= start:
                start = used_chars[char] + 1
            used_chars[char] = i

            if i - start + 1 > max_len:
                max_len = i - start + 1
                longest_sub = s[start:i+1]

        return max_len