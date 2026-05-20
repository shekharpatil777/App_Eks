from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Start with courses having no prerequisites
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        order = []

        # Topological Sort (Kahn's Algorithm)
        while q:
            node = q.popleft()
            order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
