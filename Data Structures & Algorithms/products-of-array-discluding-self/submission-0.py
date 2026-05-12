class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1]
        r = [1]
        n=len(nums)

        for i in range(n):
            l.append(l[-1]*nums[i])
            r.append(r[-1]*nums[n-i-1])
        
        res = []
        # print(l,r)
        for i in range(1,n+1):
            # print(l[i-1],r[n-i+1])
            res.append(l[i-1]*r[n-i])
        return res

        