class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        state = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)

        def dfs(node):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False

            state[node] = 1
            for nei in graph[node]:
                if dfs(nei):
                    return True

            state[node] = 2
            return False

        for i in range(numCourses):
            if dfs(i):
                return False

        return True