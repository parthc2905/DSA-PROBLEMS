class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            nums[i] = s

        for i in range(len(nums)-1):
            if (nums[i] - (nums[-1]-nums[i]))%2==0:
                count+=1

        return count 
