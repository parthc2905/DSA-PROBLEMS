class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse=True)
        # if nums[-1]<k:
        #     return -1

        # if k in nums:
        #     return len(set(nums))-1
        # else:
        #     return len(set(nums))

        ctr = defaultdict(int)             
        for num in nums: ctr[num]+= 1
        mn, ln = min(ctr), len(ctr)
        if mn < k: return -1              
        return  ln - (mn == k)
