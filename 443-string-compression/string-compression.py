class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0

        while i < len(chars):
            count = 1
            while (count + i) < len(chars) and chars[count + i] == chars[i]:
                count += 1
            chars[insert] = chars[i]
            insert += 1
            if count > 1:
                string = str(count)
                chars[insert:insert + len(string)] = list(string)
                insert += len(string)

            i += count
        return insert   