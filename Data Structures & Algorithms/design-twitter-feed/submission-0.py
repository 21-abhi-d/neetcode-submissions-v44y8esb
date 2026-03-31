class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set) # maps followers to followees
        self.tweetMap = defaultdict(list) # general map for all users
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        while minHeap and len(ret) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            ret.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)



"""
followMap = {
    userId/followerId: (followeeId1, followeeId2)
}

tweetMap = {
    userId1: [(0, tweet1), (1, tweet2)]
    userId2: [(3, tweet3), (4, tweet4)]
}

"""
