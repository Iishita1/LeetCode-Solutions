class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        if arrivalTime+delayedTime<24:
            return arrivalTime+delayedTime
        elif arrivalTime+delayedTime>=24:
            return abs(24 - (arrivalTime+delayedTime))