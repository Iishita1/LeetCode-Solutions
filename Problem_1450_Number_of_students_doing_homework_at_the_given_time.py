class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        a=0
        for i in range(0, len(startTime)):
            if queryTime<=endTime[i] and startTime[i]<=queryTime:
                a+=1
        return a