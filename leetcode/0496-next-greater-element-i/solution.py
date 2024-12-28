class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        for num1 in range(len(nums1)):
            i = nums2.index(nums1[num1])
            if i == len(nums2)-1:
                nums1[num1] = -1
            else:
                curr = i
                while (i<len(nums2)-1):
                    i+=1
                    if nums2[i] > nums2[curr]:
                        nums1[num1] = nums2[i]
                        break
                else:
                    nums1[num1] = -1

        return nums1
