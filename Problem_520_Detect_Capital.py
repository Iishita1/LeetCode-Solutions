class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper()==True:
            return True
        elif word.islower()==True:
            return True
        elif word.istitle()==True:
            return True
        else:
            return False
                