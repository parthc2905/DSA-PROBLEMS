class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s+=min(i%3,3-(i%3))
        return s
