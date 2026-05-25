class Solution:
    def reverseBits(self, n: int) -> int:
        k=0
        for i in range(32):
            k <<= 1
            k+=n&1
            n>>=1
        return k
        