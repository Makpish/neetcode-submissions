class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = set()
        for i in nums:
            x.add(i)
        
        seen = set()

        mans = 0

        for i in nums:
            if i in seen:
                continue
            a = i-1
            cans = 1
            while a in x and a not in seen:
                a-=1
                cans+=1
            a = i+1
            while a in x and a not in seen:
                a+=1
                cans+=1
            mans = max(mans, cans)
        return mans


        