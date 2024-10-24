class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = []
        n = len(nums)
        nums = list(set(nums))
        for i in range(1,n+1):
            if i not in nums:
                l.append(i)
            else:
                nums.remove(i)
        return l
