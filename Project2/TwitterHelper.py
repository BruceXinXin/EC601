import requests
import json

from USER_KEY import *


class TwitterHelper:
    def __init__(self):
        # A function jump table
        self._function_table = {
            "user_timeline": TwitterHelper._create_user_timeline_url,
            "user_data": TwitterHelper._create_user_url,
            "tweets": TwitterHelper._create_tweets_url,
            # ...
        }

    @staticmethod
    def _create_user_timeline_url(user_id):
        url = "https://api.twitter.com/2/users/{}/tweets".format(user_id)
        return url

    @staticmethod
    def _create_user_url(usernames, user_fields):
        url = "https://api.twitter.com/2/users/by?usernames={}&user.fields={}".format(usernames, user_fields)
        return url

    @staticmethod
    def _create_tweets_url(tweet_fields, ids):
        url = "https://api.twitter.com/2/tweets?ids={}&tweet.fields={}".format(ids, tweet_fields)
        return url

    @staticmethod
    def _bearer_oauth(r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
        r.headers["User-Agent"] = "v2TweetLookupPython"
        return r

    @staticmethod
    def _connect_to_endpoint(url):
        response = requests.request("GET", url, auth=TwitterHelper._bearer_oauth)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        return response.json()

    @staticmethod
    def _parse_data(url) -> str:
        json_response = TwitterHelper._connect_to_endpoint(url)
        return json.dumps(json_response, indent=4, sort_keys=True)

    def get_data(self, function: str, **kwargs) -> str:
        """
        The only interface for users to get access to data.
        :param function: The function name, see self._function_table
        :param kwargs:   The key params of the url
        :return:         The data
        """
        if function not in self._function_table.keys():
            raise ValueError("Invalid function name ({})!".format(function))

        url: str = self._function_table[function](**kwargs)
        return TwitterHelper._parse_data(url)
