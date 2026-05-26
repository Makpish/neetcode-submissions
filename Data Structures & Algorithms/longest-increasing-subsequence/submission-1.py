class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i,prev):
            if (i,prev) in dp:
                return dp[(i,prev)]
            if i==len(nums):
                return 0
            ma = 0
            for j in range(i,len(nums)):
                if nums[j]>prev:
                    ma = max(ma, 1+dfs(j+1, nums[j]))
            dp[(i,prev)] = ma
            return ma
        
        ma = 0
        for i in range(len(nums)):
            ma = max(ma, dfs(i,nums[i]-1))
        return ma
        