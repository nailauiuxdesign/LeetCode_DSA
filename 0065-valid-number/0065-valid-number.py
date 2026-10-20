class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        if not s:
            return False

        seen_num = False
        seen_dot = False
        seen_e = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_num = True
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in 'eE':
                if seen_e or not seen_num:
                    return False
                seen_e = True
                seen_num = False
            elif char in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False
                seen_num = False
            else:
                return False

        return seen_num
