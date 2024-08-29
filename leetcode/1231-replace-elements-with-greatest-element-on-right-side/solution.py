class Solution:
    def replaceElements(self, arr: List[int]):
        m = -1
        cur = 0
        for i in range(len(arr) - 1, -1, -1):
            cur = arr[i]
            arr[i] = m        
            m = max(m, cur)
        return arr
