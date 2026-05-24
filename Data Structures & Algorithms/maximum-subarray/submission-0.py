class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=max(nums)
        if m<0:
            return m
        c=nums[0]
        for i in range(1,len(nums)):
            c+=nums[i]
            if c<0:
                c=0
            m=max(m,c)
            # print(m,c)
        return m

        