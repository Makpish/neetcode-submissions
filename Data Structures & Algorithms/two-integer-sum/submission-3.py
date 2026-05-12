class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for i in range(len(nums)):
            if nums[i] in x:
                return sorted([i,x[nums[i]]])
            x[target - nums[i]] = i
        return []