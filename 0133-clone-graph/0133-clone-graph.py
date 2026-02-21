from typing import Optional
class Solution:
    def clone(self, node, visited):
        if node in visited:
            return visited[node]
        cloned_node = Node(node.val)
        visited[node] = cloned_node
        for neighbor in node.neighbors:
            cloned_node.neighbors.append(self.clone(neighbor, visited))
        return cloned_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return
        visited = {}
        return self.clone(node, visited)