class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minh = []
        self.k = k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.minh, val)
        if len(self.minh)>self.k:
            heapq.heappop(self.minh)
        return self.minh[0]
        
