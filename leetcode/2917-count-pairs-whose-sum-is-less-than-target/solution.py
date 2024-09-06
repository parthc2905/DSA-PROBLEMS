class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i,j = 0,0
        k = 0
        while(i<len(nums)-1):
            j = i+1
            while(j<len(nums)):
                if(nums[i]+nums[j]<target and i!=j):
                    k+=1
                j+=1
            i+=1
        return k

        
