class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxlen = 1
        length = 1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                length += 1
                maxlen = max(maxlen, length)
            else:
                length = 1
        return maxlen
