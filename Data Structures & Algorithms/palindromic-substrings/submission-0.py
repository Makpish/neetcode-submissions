class Solution:
    def countSubstrings(self, s: str) -> int:
        c=[0]
        def p(i,j):
            if i<0 or j==len(s) or s[i]!=s[j]:
                return
            c[0]+=1
            p(i-1, j+1)
        
        i=0
        while i<len(s):
            p(i,i)
            p(i,i+1)
            i+=1
        return c[0]
        