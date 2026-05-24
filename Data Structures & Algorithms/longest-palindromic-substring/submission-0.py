class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPallin(i,j):
            if i<0 or j==len(s) or s[i] != s[j]:
                return i+1,j-1
            return isPallin(i-1, j+1)
        
        i=0
        m1,m2 = 0,0
        while i<len(s):
            x,y = isPallin(i,i)
            x1,y1 = isPallin(i,i+1)
            if m2-m1+1<y-x+1:
                m1=x
                m2=y
            if m2-m1+1<y1-x1+1:
                m1=x1
                m2=y1
            # print(m1,m2)
            i+=1
        return s[m1:m2+1]
        