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
            
            # Decrease in-degree for all neighbor courses
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                # If neighbor has no more prerequisites, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If we finished all courses, there's no cycle
        return completed_courses == numCourses