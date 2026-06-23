class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        x = self.permute(nums[1:])
        r = []
        for y in x:
            for z in range(len(y)+1):
                r.append(y[:z] + [nums[0]] + y[z:])
        return r
        

        