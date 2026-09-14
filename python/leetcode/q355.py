from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # Global timestamp to order tweets chronologically
        self.time = 0
        # Maps userId to a list of (timestamp, tweetId) tuples
        self.tweet_map = defaultdict(list)
        # Maps userId to a set of followeeIds
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        # Max-heap elements: (-timestamp, tweetId, followeeId, next_index_in_tweets)
        max_heap = []
        
        # User always implicitly follows themselves
        followees = self.follow_map[userId] | {userId}

        # Initialize heap with the most recent tweet from each followee
        for followee_id in followees:
            tweets = self.tweet_map[followee_id]
            if tweets:
                last_idx = len(tweets) - 1
                time, tweet_id = tweets[last_idx]
                heapq.heappush(max_heap, (-time, tweet_id, followee_id, last_idx - 1))

        # Extract up to 10 most recent tweets
        while max_heap and len(res) < 10:
            neg_time, tweet_id, followee_id, next_idx = heapq.heappop(max_heap)
            res.append(tweet_id)
            
            # Push the next recent tweet from the same user if available
            if next_idx >= 0:
                time, next_tweet_id = self.tweet_map[followee_id][next_idx]
                heapq.heappush(max_heap, (-time, next_tweet_id, followee_id, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)