class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = {}
        ls = 0
        cs = 0
        i=0
        while i<len(s):
            if s[i] not in x:
                x[s[i]] = i
                cs+=1
                ls = max(ls, cs)
            else:
                pi = x[s[i]]
                t=cs - (i-pi)
                print(t,i,cs,pi)
                while t>=0:
                    x.pop(s[pi-t], None)
                    t-=1
                x[s[i]] = i
                cs = i-pi
            i+=1
        return ls
                
        