class Solution:
    def groupThePeople(self, groupSizes: list) -> list:
        sizeMap = {}
        for index, size in enumerate(groupSizes):
            if size in sizeMap.keys():
                sizeMap[size].append(index)
            else:
                sizeMap[size] = [index]
        retList = []
        for key, value in sizeMap.items():
            for index in range(len(value) // key):
                retList.append(value[index * key:(index + 1) * key])
        return retList


sol = Solution()
print(sol.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
