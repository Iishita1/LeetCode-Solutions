class Solution:
    def repeatedCharacter(self, s: str) -> str:
        first_occurrence = {}
        for i, char in enumerate(s):
            if char in first_occurrence:
                return char
            first_occurrence[char] = i
        return ""  # unreachable per constraints