class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in s:
            if i in ["(", "{", "["]:
                st.append(i)
            else:
                if len(st)<1:
                    return False
                if i == ")":
                    if st[-1] != "(":
                        return False
                    st.pop()
                elif i == "}":
                    if st[-1] != "{":
                        return False
                    st.pop()
                elif i == "]":
                    if st[-1] != "[":
                        return False
                    st.pop()
        return len(st)==0

        