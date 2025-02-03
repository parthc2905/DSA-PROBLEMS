class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        countinc = 1
        m = 1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                countinc+=1
                m = max(m,countinc)
            else:
                countinc = 1

        
        countdec = 1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                countdec+=1
                m = max(m,countdec)
            else:
                countdec = 1
        
        return m
