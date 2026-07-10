class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i=="+":
                x=st.pop()
                y=st.pop()
                st.append(y+x)
            elif i=="-":
                x=st.pop()
                y=st.pop()
                st.append(y-x)
            elif i=="*":
                x=st.pop()
                y=st.pop()
                st.append(y*x)
            elif i=="/":
                x=st.pop()
                y=st.pop()
                s=1
                if x<0:
                    s*=-1
                if y<0:
                    s*=-1
                st.append(s*(abs(y)//abs(x)))
            else:
                st.append(int(i))
        return st.pop()
        