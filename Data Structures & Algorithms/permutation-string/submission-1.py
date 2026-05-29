class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        ls1 = [0]*26
        ls2 = [0]*26

        for i in range(len(s1)):
            ls1[ord(s1[i])-97]+=1
            ls2[ord(s2[i])-97]+=1
        
        i = len(s1)

        while i<len(s2):
            if ls1 == ls2:
                return True
            
            ls2[ord(s2[i])-97]+=1
            ls2[ord(s2[i-len(s1)])-97]-=1
            i+=1
        
        return ls1==ls2
        