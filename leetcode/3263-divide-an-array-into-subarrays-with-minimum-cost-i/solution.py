class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s = nums[0]
        nums[1:] = sorted(nums[1:])
        s = s + nums[1] + nums[2]
        return s
