import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}       # userId -> [(time, tweetId)]
        self.following = {}    # userId -> set of followed users
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Create the user's tweet list if needed
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        heap = []

        # Include the user and everyone they follow
        users = {userId}

        if userId in self.following:
            users.update(self.following[userId])

        # Add each user's newest tweet to the heap
        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                # Negative time puts newest tweets first
                heapq.heappush(heap, (-time, tweetId, user, index))

        # Get the 10 most recent tweets
        while heap and len(result) < 10:
            negTime, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)

            # Add the next older tweet from that user
            if index > 0:
                index -= 1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(heap, (-time, tweetId, user, index))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # Create a set if the follower isn't in the dictionary
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)