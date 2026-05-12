from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. Build the adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # 2. Add all courses with no prerequisites to the queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 3. Process the courses
        completed_courses = 0
        while queue:
            current = queue.popleft()
            completed_courses += 1
