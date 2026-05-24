class Solution:
    def rob(self, nums: List[int]) -> int:
        a=0
        b=nums[0]
        i=1
        n=len(nums)
        while i<n:
            b,a = max(b, nums[i]+a), b
            i+=1
        return b
        