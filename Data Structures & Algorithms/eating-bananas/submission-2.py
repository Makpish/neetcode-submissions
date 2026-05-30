class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = max(1,sum(piles)//h)
        ans = r

        while l<=r:
            k = (l+r)//2
            nh = sum([-(-p // k)  for p in piles])
            # print(l,r,k,nh)
            if nh>h:
                l=k+1
            else:
                ans = min(ans,k)
                r=k-1
        return ans

        