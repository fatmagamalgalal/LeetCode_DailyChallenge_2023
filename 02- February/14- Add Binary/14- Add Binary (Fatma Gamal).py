// Author: Fatma Gamal Eldin Galal
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # read the two number as binary representation
        x = int(a, 2)
        y = int(b,2)
        # print(x, y)
        return bin(x + y)[2:]
