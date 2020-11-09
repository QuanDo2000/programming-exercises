class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        mapVar = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in mapVar.keys() and i != mapVar[complement]):
                return [i, mapVar[complement]]
            mapVar[nums[i]] = i
