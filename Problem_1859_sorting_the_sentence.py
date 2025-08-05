class Solution:
    def sortSentence(self, s: str) -> str:
        k=s.split()
        j=[None]*len(k)
        for i in k:
            inc=int(i[-1])-1
            j[inc]=i[:-1]
        return " ".join(j)