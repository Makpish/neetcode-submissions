class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = [0]*(n+1)
        r = [0]*(n+1)

        for i in range(n):
            if heights[i] > l[i]:
                l[i+1] = heights[i]
            else:
                l[i+1] = l[i]
        
        for i in range(n-1,-1,-1):
            if heights[i]>r[i+1]:
                r[i] = heights[i]
            else:
                r[i] = r[i+1]
        # print(l,r)
        
        m=0
        i=0
        j=n
        while i<=j:
            m = max(m, (j-i+1)*min(l[i],r[j]))
            # print(l[i],r[j])
            # print(i,j)
            if l[i]<r[j]:
                i+=1
            else:
                j-=1
            # print(i,j)

        return m

            
        