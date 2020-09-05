class Solution:
    def permute(self, nums: list) -> list:
        return self.permListRec(nums)

    def permuteRec(self, inputList):
        if len(inputList) == 0:
            return []
        if len(inputList) == 1:
            return [inputList]

        retList = []
        for i in range(len(inputList)):
            m = inputList[i]

            remList = inputList[:i] + inputList[i+1:]

            for p in self.permListRec(remList):
                retList.append([m] + p)
        return retList

    def permuteBacktrack(self, inputList, retList, index):
        if index == (len(inputList) - 1):
            retList.append(inputList[:])
        for i in range(index, len(inputList)):
            inputList[i], inputList[index] = inputList[index], inputList[i]
            self.permuteBacktrack(inputList, retList, index + 1)
            inputList[i], inputList[index] = inputList[index], inputList[i]

    def permuteBacktrackMain(self, inputList):
        retList = []
        self.permuteBacktrack(inputList, retList, 0)
        return retList
