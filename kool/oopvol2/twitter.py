"""Twitter."""
import re

class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """

    tweet_and_speed = []
    for tweet in tweets:
        speed = float(tweet.retweets/tweet.time)
        tweet_and_speed.append([tweet,speed])

    fastest = max(tweet_and_speed, key= lambda x:x[1])
    return fastest[0]

def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    return sorted(tweets, key=lambda tweet:(-tweet.retweets, tweet.time))

def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    tweets_with_hashtag = []
    for tweet in tweets:
        if hashtag in tweet.content:
            tweets_with_hashtag.append(tweet)
    return tweets_with_hashtag

def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """

    """
    The regex pattern #\w+ matches any hashtag starting with #
    followed by one or more word characters (letters, digits, or underscores).
    The re.findall function returns all non-overlapping matches of the pattern in the string as a list.
    """
    # store tags and popularity in dict
    allhashtags_and_popularity = dict()
    for tweet in tweets:
        hashtags_in_tweet = re.findall(r'#\w+', tweet.content)
        if hashtags_in_tweet:
            for htag in hashtags_in_tweet:
                if htag in allhashtags_and_popularity:
                    allhashtags_and_popularity[htag] += tweet.retweets
                else:
                    allhashtags_and_popularity[htag] = tweet.retweets
    # convert dict to list and sort by retweets descending, in case of tie by hastag
    resultlist = list(allhashtags_and_popularity.items())
    resultlist_sorted = sorted(resultlist, key=lambda x:(-x[1],x[0]))
    # return only the hastag in final list
    final_list = [item[0] for item in resultlist_sorted]
    return final_list

if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"

