class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minhp = []

        for n in nums:
            heapq.heappush(minhp, n)
            if len(minhp)>k:
                heapq.heappop(minhp)
        
        return minhp[0]

        