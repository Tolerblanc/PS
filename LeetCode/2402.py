from heapq import heapify, heappush, heappop
from collections import Counter


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        availableRooms = [i for i in range(n)]
        heapify(availableRooms)
        cnt = Counter()
        meetingEnds = []  # (endtime, roomNumber)

        for start, end in meetings:
            while meetingEnds and meetingEnds[0][0] <= start:
                _, prevRoom = heappop(meetingEnds)
                heappush(availableRooms, prevRoom)
            if not availableRooms:
                prevEnd, prevRoom = heappop(meetingEnds)
                heappush(availableRooms, prevRoom)
                end += prevEnd - start
            currRoom = heappop(availableRooms)
            cnt[currRoom] += 1
            heappush(meetingEnds, (end, currRoom))
        return cnt.most_common()[0][0]
