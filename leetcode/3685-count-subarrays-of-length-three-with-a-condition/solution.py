class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            if (nums[i:i+3][0] + nums[i:i+3][-1])*2 == (nums[i:i+3][1]):
                count+=1
        
        return count
