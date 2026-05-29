class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxh = []
        n=len(nums)
        hmap = {}

        for i in range(k):
            heapq.heappush(maxh, -nums[i])
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)
        
        res = [-maxh[0]]
        i=k

        while i<n:
            heapq.heappush(maxh, -nums[i])
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)
            x = nums[i-k]
            # print(hmap)
            hmap[x] -= 1

            while hmap[-maxh[0]] < 1:
                y = -heapq.heappop(maxh)
                hmap[y] -= 1
            
            res.append(-maxh[0])
            i+=1
        return res


        