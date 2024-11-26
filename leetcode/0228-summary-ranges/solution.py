class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = []
        if len(nums)>0:
            start = nums[0]
            end = nums[0]
            i = 1
            while i<len(nums):

                if nums[i] == end + 1:
                    end = nums[i]
                else:
                    if start == end :
                        l.append(str(start))
                    else:
                        l.append(str(start)+"->"+str(end))
                    start = nums[i]
                    end = start

                i+=1
        
            if start == end :
                l.append(str(start))
            else:
                l.append(str(start)+"->"+str(end))


        return l
