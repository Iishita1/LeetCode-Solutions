class Solution:
  def largestPalindromic(self, num: str) -> str:
    count = Counter(num)
    left = []
    mid = ''

    # Traverse digits in reverse for largest first
    for digit in reversed('0123456789'):
        pairs = count[digit] // 2
        if pairs:
            left.append(digit * pairs)
            count[digit] -= 2 * pairs

    # Pick the largest possible middle digit
    for digit in reversed('0123456789'):
        if count[digit]:
            mid = digit
            break

    left_part = ''.join(left)
    # Remove leading zero unless it is the only digit
    if left_part and left_part[0] == '0':
        return mid if mid else '0'

    return left_part + mid + left_part[::-1] if left_part or mid else '0'