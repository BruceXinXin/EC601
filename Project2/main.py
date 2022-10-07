import json

from TwitterHelper import TwitterHelper


if __name__ == "__main__":
    t_helper = TwitterHelper()

    # user data
    user_data = t_helper.get_data("user_data", usernames="AP", user_fields="description,created_at")
    print(user_data)

    print("######################################################")

    # extract user id
    user_id = json.loads(user_data)["data"][0]["id"]
    print(user_id)

    print("######################################################")

    # user timeline
    user_timeline = t_helper.get_data("user_timeline", user_id=user_id)
    print(user_timeline)

    print("######################################################")

    # extract tweets id
    tid = []
    data_list = json.loads(user_timeline)["data"]
    for data in data_list:
        tid.append(data["id"])

    # tweets by id
    print(t_helper.get_data("tweets",
                            tweet_fields="lang,created_at,text,author_id", ids=",".join(tid)))

    print("######################################################")
