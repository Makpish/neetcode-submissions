class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            a = [0]*26
            for i in s:
                a[ord(i)-97]+=1
            
            a = tuple(a)
            if a not in hmap:
                hmap[a]=[]
            hmap[a].append(s)
        
        return [i for i in hmap.values()]
        