# from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        m = 0
        nums.sort()
        res = 0
        i = nums[0]
        for j in nums:
            if i==j:
                c+=1
            else:
                i = j
                c = 1
            
            if c > m:
                m = c
                res = j
        return res
        
        # return Counter(nums).most_common(1)[0][0]
