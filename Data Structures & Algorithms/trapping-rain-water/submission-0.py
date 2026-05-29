class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0]
        r = [0]
        n = len(height)
        for i in range(n):
            l.append(max(height[i],l[-1]))
            r.append(max(height[n-i-1],r[-1]))
        
        r = r[::-1]
        water = 0
        for i in range(n):
            # print(l[i],r[i+1])
            water += max(0,min(l[i],r[i+1])-height[i])
        return water
        