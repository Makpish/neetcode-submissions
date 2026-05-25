class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        k = n*(n+1)//2
        for i in nums:
            k-=i
        return k
        