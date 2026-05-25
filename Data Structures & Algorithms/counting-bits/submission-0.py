class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            c=0
            while n:
                if n%2!=0:
                    c+=1
                n=n//2
            return c
        res = []
        for i in range(n+1):
            res.append(hammingWeight(i))
        return res

        