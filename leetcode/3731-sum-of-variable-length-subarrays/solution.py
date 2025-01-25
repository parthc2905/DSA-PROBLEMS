class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        s = 0

        for i in range(len(nums)):
            j = max(0,i-nums[i])
            s += sum(nums[j:i+1])

        return s
