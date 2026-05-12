class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        f = [[] for i in range(len(nums)+1)]

        for i in nums:
            x[i] = 1+x.get(i,0)
        
        for i in x.keys():
            f[x[i]].append(i)
        
        res = []
        for i in range(len(nums),-1,-1):
            for j in f[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res
        