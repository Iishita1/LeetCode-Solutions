class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures = {path[0] for path in paths}
        for _, destination in paths:
            if destination not in departures:
                return destination