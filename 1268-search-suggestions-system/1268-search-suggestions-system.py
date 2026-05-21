class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def suggestedProducts(self, products, searchWord):
        root = TrieNode()
        result = []
        
        products.sort()

        for word in products:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        def dfs(node, words):
            if not node or len(words) == 3:
                return
            if node.word:
                words.append(node.word)
            for ch in node.children:
                dfs(node.children[ch], words)

        node = root

        for ch in searchWord:
            words = []
            if node and ch in node.children:
                node = node.children[ch]
                dfs(node, words)
            else:
                node = None
            result.append(words)

        return result
