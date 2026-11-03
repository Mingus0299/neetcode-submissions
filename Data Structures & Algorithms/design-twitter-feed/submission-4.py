class Twitter:

    def __init__(self):
        self.posttweet = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posttweet[userId].append([self.time,tweetId])
        self.time-=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        maxH = []
        self.following[userId].add(userId)
        for follower in self.following[userId]:
            if not self.posttweet[follower]:
                continue
            idx = len(self.posttweet[follower]) - 1
            time , tweetId = self.posttweet[follower][idx]
            heapq.heappush(maxH, [time, tweetId, follower, idx])

        res = []
        
        while maxH and len(res) < 10:
            time, tweetId, follower, idx = heapq.heappop(maxH)
            res.append(tweetId)
            idx-=1
            if idx >= 0:
                time, tweetId  = self.posttweet[follower][idx]
                heapq.heappush(maxH, [time, tweetId, follower, idx])

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)        
