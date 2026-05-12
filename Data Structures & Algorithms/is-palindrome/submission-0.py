class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<j:
            x = ord(s[i])
            if not ((x>47 and x<58) or (x>64 and x<91) or (x>96 and x<123)):
                i+=1
                continue
            x = ord(s[j])
            if not ((x>47 and x<58) or (x>64 and x<91) or (x>96 and x<123)):
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
        