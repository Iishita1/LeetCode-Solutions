class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=list(zip(names,heights))
        n.sort(key=lambda x: x[1], reverse=True)
        return [name for name, _ in n]