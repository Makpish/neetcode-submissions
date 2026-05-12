class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        # print(nums)

        i=0
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                x = nums[k] + nums[i] + nums[j]
                # print(x,(nums[i],nums[j],nums[k]))
                if x == 0:
                    seen.add((nums[i],nums[j],nums[k]))
                if x>0:
                    k-=1
                else:
                    j+=1
            i+=1
        return list(seen)


        