class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=celsius + 273.15
        farenheit = celsius * 1.80 + 32.00
        l=[kelvin,farenheit]
        return l
