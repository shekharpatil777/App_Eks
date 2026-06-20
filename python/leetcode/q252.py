class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda x: x[0])
