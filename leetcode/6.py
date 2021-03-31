class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for i in range(numRows)]

        counter = 0
        inc = 1
        for index in range(len(s)):
            ans[counter].append(s[index])
            if counter == 0:
                inc = 1
            elif counter == numRows - 1:
                inc = -1
            counter += inc
        ans = [''.join(x) for x in ans]
        return ''.join(ans)
