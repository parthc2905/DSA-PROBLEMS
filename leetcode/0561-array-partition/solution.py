class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxsum = sum(nums[::2])
        return maxsum
        
