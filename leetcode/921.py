class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count_left = 0
        count_right = 0
        for char in S:
            if char == '(':
                count_left += 1
            if char == ')':
                if count_left > 0:
                    count_left -= 1
                else:
                    count_right += 1
        return count_left + count_right
