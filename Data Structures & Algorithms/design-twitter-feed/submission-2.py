class Twitter:

    def __init__(self):
        self.followmap = {}
        self.tweetmap = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetmap:
            self.tweetmap[userId] = []
        self.tweetmap[userId].append([self.count, tweetId])
        # print(self.tweetmap)
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        minh = []
        followees = self.followmap.get(userId, set())
        followees.add(userId)
        # print(followees)
        for f in followees:
            tweets = self.tweetmap.get(f,[])[-10:]
            for c,t in tweets:
                heapq.heappush(minh, [-c,t])
                if len(minh)>10:
                    heapq.heappop(minh)
        res = []
        while minh:
            res.append(heapq.heappop(minh)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = set()
        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap or followeeId not in self.followmap[followerId]:
            return
        self.followmap[followerId].remove(followeeId)
        
