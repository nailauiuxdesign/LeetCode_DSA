class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        result = []

        while len(s) > k:
            result.append(s[-k:])
            s = s[:-k]
        if s:
            result.append(s)

        return "-".join(result[::-1])