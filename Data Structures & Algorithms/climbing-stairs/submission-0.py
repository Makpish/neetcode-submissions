class Solution:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        while n:
            temp = a+b
            a=b
            b=temp
            n-=1
        return b
        