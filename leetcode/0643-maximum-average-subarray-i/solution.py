class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        init = sum(nums[:k])
        maxavg = init/k
        for i in range(1,len(nums)-k+1):
            init -= nums[i-1]
            init += nums[i+k-1]
            # maxavg = max(init/k, maxavg)
            if (init/k) > maxavg:
                maxavg = init/k
        
        return maxavg
