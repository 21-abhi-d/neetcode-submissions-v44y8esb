"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])

        i = 0 
        j = 0
        count = 0
        max_rooms = 0
        while i < len(start_times):
            if start_times[i] < end_times[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            max_rooms = max(count, max_rooms)
        
        return max_rooms

