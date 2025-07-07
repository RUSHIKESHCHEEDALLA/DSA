import heapq
class Solution(object):
    def maxEvents(self, events):
        events.sort() 
        min_heap = []  
        i = 0         
        res = 0        
        day = 1        
        n = len(events)
        # print(events)
        while i < n or min_heap:
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])   
                i += 1
            # print(min_heap)
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            # print(min_heap)
            if min_heap:
                heapq.heappop(min_heap)  
                res += 1
            # print(min_heap)

            day += 1

        return res
        