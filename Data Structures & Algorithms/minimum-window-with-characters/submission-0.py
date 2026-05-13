class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        smap = {}
        for i in t:
            tmap[i] = 1 + tmap.get(i,0)
        
        l = 0
        x=0
        ma = len(s)+1
        res = ""
        for r in range(len(s)):
            if s[r] not in tmap:
                continue
            
            smap[s[r]] = 1 + smap.get(s[r],0)
            if smap[s[r]] <= tmap[s[r]]:
                x+=1
            
            while s[l] not in tmap or smap[s[l]]>tmap[s[l]]:
                if s[l] in tmap:
                    smap[s[l]] -= 1
                l+=1
            
            if x==len(t) and r-l+1<ma:
                res = s[l:r+1]
                ma = r-l+1
        return res
        
                

            


        

        