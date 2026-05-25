class Solution:
    def reverseBits(self, n: int) -> int:
        k=0
        for i in range(32):
            k = k*2 + n%2
            n//=2
        return k
        