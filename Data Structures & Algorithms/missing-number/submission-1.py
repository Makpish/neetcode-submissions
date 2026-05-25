class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        for i in nums:
            k^=i
            # print(k)
        for i in range(1,n+1):
            k^=i
        return k
        