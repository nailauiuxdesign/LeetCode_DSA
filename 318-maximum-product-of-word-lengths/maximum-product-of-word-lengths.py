class Solution:
    def maxProduct(self, words: list[str]) -> int:
        masks = []

        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)

        max_product = 0
        for i in range(len(words)):
            for j in range(i):
                if masks[i] & masks[j] == 0:
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)

        return max_product