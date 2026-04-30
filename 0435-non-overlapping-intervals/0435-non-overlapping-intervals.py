class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        removed = 0

        for start, finish in intervals[1:]:
            if start >= end:
                end = finish
            else:
                removed += 1

        return removed