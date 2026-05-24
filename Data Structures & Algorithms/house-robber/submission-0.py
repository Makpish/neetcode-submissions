class Solution:
    def rob(self, nums: List[int]) -> int:
        a=0
        b=nums[0]
        i=1
        while i<len(nums):
            temp = max(b, nums[i]+a)
            a = b
            b = temp
            i+=1
        return b
        