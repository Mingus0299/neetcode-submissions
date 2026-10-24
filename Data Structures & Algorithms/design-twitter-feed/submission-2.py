class Twitter:

    def __init__(self):
        self.mappostTweet = defaultdict(list)
        self.mapfollows = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.mappostTweet[userId].append([self.time, tweetId])
        self.time-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxH = []
        heapq.heapify(maxH)
        self.mapfollows[userId].add(userId)
        for following in self.mapfollows[userId]:
            if not self.mappostTweet[following]:
                continue
            index = len(self.mappostTweet[following]) - 1
            time, tweetId = self.mappostTweet[following][index]
            heapq.heappush(maxH, [time, tweetId, following, index])
        
        res = []
        while maxH and len(res) <10:
            time, tweetId, following, index = heapq.heappop(maxH)
            res.append(tweetId)
            index-=1

            if index >= 0:
                time, tweetId = self.mappostTweet[following][index]
                heapq.heappush(maxH, [time, tweetId, following, index])

        return res

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.mapfollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.mapfollows[followerId]:
            self.mapfollows[followerId].remove(followeeId)
