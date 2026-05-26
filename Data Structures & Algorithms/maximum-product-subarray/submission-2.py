class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax,cmin = 1,1
        res = max(nums)
        for i in nums:
            if i==0:
                cmax,cmin = 1,1
            else:
                tmp = cmax*i
                cmax = max(tmp,cmin*i,i)
                cmin = min(tmp,cmin*i,i)
                res = max(res,cmax)
        return res


        