class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # XOR all numbers to get the XOR of the two unique numbers
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        
        # Find the rightmost set bit
        diff_bit = xor_sum & -xor_sum
        
        # Partition the numbers into two groups and find each unique number
        num1, num2 = 0, 0
        for num in nums:
            if num & diff_bit:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]