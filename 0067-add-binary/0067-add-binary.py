class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = int(a, 2) + int (b, 2) 
        # This converts binary string a into a decimal number.
        return bin (result)[2:] 
        # bin (result) converts the result back into binary, but it returns a string like '0b100'
        #The [2:] part removes the '0b' prefix.

