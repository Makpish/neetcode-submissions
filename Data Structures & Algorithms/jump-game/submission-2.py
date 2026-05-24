class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j=nums[0]
        i=1
        while i<len(nums):
            if j<i:
                return False
            j=max(j,i+nums[i])
            i+=1
        return j>=len(nums)-1
        