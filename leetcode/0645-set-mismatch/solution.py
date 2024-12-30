# from collections import Counter
# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
        # arr = [0,0]
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         arr[1] = i
        #         break
        
        # c = Counter(nums)
        # arr[0] = c.most_common()[0][0]
        # return arr
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = 0, 0
        for i in range(len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                duplicate = i
            elif count == 0:
                missing = i
        return [duplicate, missing]
