from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # l = 0
        # nums = Counter(nums)
        # num = list(set(nums))
        # num.sort()
        # for i in range(len(num)-1):
        #     if num[i+1]-num[i]==1:
        #         l = max(l, nums[num[i+1]]+nums[num[i]])
        
        # return l
        count = Counter(nums)
        
        max_len = 0
        for num in count:
            if num + 1 in count: 
                max_len = max(max_len, count[num] + count[num + 1])  
        
        return max_len

