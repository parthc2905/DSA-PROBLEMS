class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m = 0
        s = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                s+=nums[i]
            else:
                m = max(s,m)
                s = nums[i]
        
        m = max(s,m)
        return m
