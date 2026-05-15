class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        n=len(nums)
        r=n-1

        while l<r:
            m = (l+r)//2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        p = l
        # print(p)

        if target > nums[n-1]:
            l = 0
            r = p-1
        else:
            l = p
            r = n-1
        
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1

        
        