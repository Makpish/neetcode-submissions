class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = [[position[i],speed[i]] for i in range(len(position))]
        s.sort()

        c = 1
        t = (target-s[-1][0])/s[-1][1]

        i=len(s)-2
        while i>=0:
            nt = (target-s[i][0])/s[i][1]
            if nt>t:
                c+=1
                t=nt
            i-=1
        return c

        