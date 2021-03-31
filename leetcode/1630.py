class Solution:
    def check_arith(self, nums):
        nums.sort()
        diff = nums[1] - nums[0]
        prev = nums[0]
        for num in nums[1:]:
            if num - prev != diff:
                return False
            prev = num
        return True

    def checkArithmeticSubarrays(self, nums: list, l: list, r: list) -> list:
        ans = []
        for l_idx, r_idx in zip(l, r):
            ans.append(self.check_arith(nums[l_idx:r_idx + 1]))
        return ans
