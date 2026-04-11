from collections import defaultdict

class Solution:
    def minReorder(self, n, connections):
        
        graph = defaultdict(list)
        original = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            original.add((a, b))

        visited = set([0])
        stack = [0]
        changes = 0

        while stack:
            city = stack.pop()

            for next_city in graph[city]:
                if next_city in visited:
                    continue

                visited.add(next_city)

                if (next_city, city) not in original:
                    changes += 1

                stack.append(next_city)

        return changes