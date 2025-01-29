class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        
        index = events[0][0]
        press = events[0][1]

        for i in range(1,len(events)):
            if events[i][1] - events[i-1][1] == press:
                index = min(events[i][0],index)
                continue
            if events[i][1] - events[i-1][1] > press:
                press = events[i][1] - events[i-1][1]
                index = events[i][0]
            
            
        return index

