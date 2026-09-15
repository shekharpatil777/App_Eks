from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        # userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # userId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrementing time creates a natural max-heap order using heapq
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # A user sees their own tweets + tweets of users they follow
        users_to_check = self.following[userId] | {userId}
        
        # Grab the last 10 tweets per relevant user (reversed so latest come first)
        recent_tweet_lists = [
            reversed(self.tweets[u][-10:]) 
            for u in users_to_check 
            if u in self.tweets and self.tweets[u]
        ]
        
        # Merge sorted iterators by timestamp (min timestamp first because self.time is negative)
        merged = heapq.merge(*recent_tweet_lists, key=lambda x: x[0])
        
        feed = []
        for _ in range(10):
            tweet = next(merged, None)
            if tweet is None:
                break
            feed.append(tweet[1])
            
        return feed
