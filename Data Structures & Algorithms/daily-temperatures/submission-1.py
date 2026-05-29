class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        st = []
        c=0
        while temperatures:
            x = temperatures.pop()
            while st and st[-1][0]<=x:
                st.pop()
            if not st:
                res.append(0)
            else:
                res.append(c-st[-1][1])
            st.append([x,c])
            c+=1
        return res[::-1]
            
        