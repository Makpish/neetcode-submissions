class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m = (l+r)//2

            if nums[r]>nums[m]:
                r=m
            else:
                l=m
            if l+1==r:
                return min(nums[l], nums[r])
        return nums[l]
        