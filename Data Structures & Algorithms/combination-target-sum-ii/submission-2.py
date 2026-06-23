# from functools import cache
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # s = set()
        candidates.sort()
        arr=[]

        # @cache
        def dfs(i,rem):
            if rem==0:
                res.append(arr.copy())
                return
            if rem<0 or i == len(candidates):
                return
            arr.append(candidates[i])
            dfs(i+1, rem-candidates[i])
            arr.pop()
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, rem)
        
        dfs(0,target)
        return res

        