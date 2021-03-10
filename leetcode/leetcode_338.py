class Solution:
    def countBits(self, num):
        ret_arr = [0]
        if num > 0:
            while len(ret_arr) < num + 1:
                ret_arr.extend([x + 1 for x in ret_arr])

        return ret_arr[0:num + 1]


sol = Solution()
print(sol.countBits(5))
