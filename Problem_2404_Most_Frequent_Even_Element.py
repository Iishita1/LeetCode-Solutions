from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_counts = Counter()
        for num in nums:
            if num % 2 == 0:  # Check if the number is even
                even_counts[num] += 1

        if not even_counts:  # No even elements found
            return -1

    # Find the element(s) with the highest frequency
        max_freq = 0
        most_frequent = -1
    
    # Iterate through the even elements and their counts
        for element, count in even_counts.items():
            if count > max_freq:
                max_freq = count
                most_frequent = element
            elif count == max_freq:
            # If frequencies are tied, return the smallest element
                most_frequent = min(most_frequent, element)

        return most_frequent