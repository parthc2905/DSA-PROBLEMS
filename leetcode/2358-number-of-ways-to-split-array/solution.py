class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        s = 0
        sums = sum(nums)
        for i in range(len(nums)-1):
            s += nums[i]
            if s>=sums-s:
                count+=1
        return count
