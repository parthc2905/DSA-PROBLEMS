class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concate = 0
        i = 0
        while i<len(nums)//2:
            concate += int(str(nums[i])+str(nums[-1-i]))
            i+=1
        if len(nums)%2:
            concate += nums[i]
        return concate
