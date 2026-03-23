class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        init = sum(nums[:k])
        maxavg = init
        for i in range(1,len(nums)-k+1):
            init -= nums[i-1]
            init += nums[i+k-1]
            maxavg = max(init, maxavg)
        
        return maxavg/k
