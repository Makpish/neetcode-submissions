class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        while n:
            if n%2!=0:
                c+=1
            n=n//2
        return c
        