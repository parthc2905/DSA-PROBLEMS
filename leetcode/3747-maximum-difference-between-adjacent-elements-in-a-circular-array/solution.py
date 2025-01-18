class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            a = max(a,abs(nums[i]-nums[i-1]))
        return a
