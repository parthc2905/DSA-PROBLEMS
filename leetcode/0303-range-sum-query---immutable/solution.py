class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        s = [0] * (n+1)
        for i, x in enumerate(nums):
            s[i+1] = s[i] + x
        self.s = s
        return

    def sumRange(self, left: int, right: int) -> int:
        return  self.s[right+1] - self.s[left]

