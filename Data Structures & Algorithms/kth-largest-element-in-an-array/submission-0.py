class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = []
        for i in nums:
            heapq.heappush(mh,i)
            if len(mh)>k:
                heapq.heappop(mh)
        return mh[0]
        