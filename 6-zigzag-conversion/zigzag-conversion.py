class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = []
        n = len(s)
        chars = 2 * (numRows - 1)

        for curr_row in range(numRows):
            index = curr_row
            
            while index < n:
                rows.append(s[index])

                if curr_row != 0 and curr_row != numRows - 1:
                    second_index = index + chars - 2 * curr_row

                    if second_index < n:
                        rows.append(s[second_index])

                index += chars

        return "".join(rows)