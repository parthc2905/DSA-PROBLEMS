class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # if len(nums)-len(set(nums))>0:
        #     return True
        # else:
        #     return False

        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        
        for i in d.values():
            if i//2>=1:
                return True
        
        return False
            
