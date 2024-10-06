class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                zero +=1
                nums.append(0)

        for i in range(zero):
            nums.remove(0)

