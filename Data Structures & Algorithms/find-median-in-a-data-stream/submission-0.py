class MedianFinder:

    def __init__(self):
        self.n = 0
        self.minh = []
        self.maxh = []
        

    def addNum(self, num: int) -> None:
        if len(self.minh)>0 and num >= self.minh[0]:
            heapq.heappush(self.minh, num)
        else:
            heapq.heappush(self.maxh, -num)
        self.n+=1

        while abs(len(self.minh) - len(self.maxh)) > self.n % 2:
            # print(abs(len(self.minh) - len(self.maxh)), self.n % 2)
            if len(self.minh)>len(self.maxh):
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
            else:
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))
            # if 
        

    def findMedian(self) -> float:
        # print(self.minh, self.maxh)
        if self.n % 2 == 0:
            return (self.minh[0] - self.maxh[0])/2
        else:
            if len(self.minh) > len(self.maxh):
                return self.minh[0]
            return -self.maxh[0]
        
        