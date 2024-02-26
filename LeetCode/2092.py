from heapq import heappush, heappop, heapify
from collections import defaultdict


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        end_time = 0
        for a, b, cost in meetings + [[0, firstPerson, 0]]:
            graph[a].append((cost, b))
            graph[b].append((cost, a))
            end_time = max(end_time, cost)
        dist = [-1] * n
        dist[0] = dist[firstPerson] = 0
        q = graph[0][:] + [(0, 0)]
        heapify(q)
        while q:
            prev_cost, prev = heappop(q)
            if dist[prev] != -1 and dist[prev] < prev_cost:
                continue
            for curr_cost, curr in graph[prev]:
                if prev_cost > curr_cost:
                    continue
                if dist[curr] == -1 or dist[curr] > curr_cost:
                    dist[curr] = curr_cost
                    heappush(q, (dist[curr], curr))
        return [idx for idx, dist in enumerate(dist) if dist != -1 and dist <= end_time]
