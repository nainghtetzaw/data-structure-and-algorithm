from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list) # {userId:[timestamp,tweetId]}
        self.followers = defaultdict(list) # {userId: [followeeId]}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append([self.timestamp, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = [] # [timestamp, tweetId]
        minHeap += self.tweets[userId]
        
        for i in self.followers[userId]:
            minHeap += self.tweets[i]
        
        heapq.heapify(minHeap)

        res = []
        for t, tweetId in heapq.nlargest(10, minHeap):
            res.append(tweetId)

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)