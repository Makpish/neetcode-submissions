class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = [[l,i] for i,l in enumerate(nums)]
        x.sort()

        i=0
        j=len(nums)-1
        
        while i<j:
            c = x[i][0]+x[j][0]
            if c==target:
                return sorted([x[i][1],x[j][1]])
            if c<target:
                i+=1
            else:
                j-=1
        
        return []
        