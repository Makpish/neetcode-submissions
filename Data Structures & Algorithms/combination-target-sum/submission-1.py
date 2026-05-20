class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def recur(i,t,l):
            if t==0:
                res.append(l[:])
                return
            
            for a in range(i,len(nums)):
                if nums[a]>t:
                    break
                l.append(nums[a])
                recur(a, t-nums[a], l)
                l.pop()
        
        recur(0,target,[])
        return res



        