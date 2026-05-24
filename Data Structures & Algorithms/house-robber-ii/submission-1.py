class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        a=0
        b=nums[0]
        i=1
        while i<n-1:
            b,a = max(b, nums[i]+a), b
            i+=1
        m=b
        a=0
        b=nums[1]
        i=2
        while i<n:
            b,a = max(b, nums[i]+a), b
            i+=1
        return max(m,b)
        