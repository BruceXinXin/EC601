The twitter analyze program.

For the convenience, I encapsulated Twitter operation into a class 'TwitterHelper'.
It can help you construct url and authorize, then you can get the results.

In the future, I can support more url format to make it more general.

Providing some results:

```python
import json
from TwitterHelper import TwitterHelper

t_helper = TwitterHelper()

user_data = t_helper.get_data("user_data", usernames="AP", user_fields="description,created_at")
user_id = json.loads(user_data)["data"][0]["id"]

user_timeline = t_helper.get_data("user_timeline", user_id=user_id)

tid = []
data_list = json.loads(user_timeline)["data"]
for data in data_list:
    tid.append(data["id"])

print(t_helper.get_data("tweets", tweet_fields="lang,created_at,text,author_id", ids=",".join(tid)))

```

```json
[
    {
        "author_id": "51241574",
        "created_at": "2022-12-20T03:00:11.000Z",
        "edit_history_tweet_ids": [
            "1605035305471557632"
        ],
        "id": "1605035305471557632",
        "lang": "en",
        "text": "Musk's Twitter rules: A dizzying, whiplash-inducing timeline https://t.co/SCuyrvI3vR https://t.co/ioZAAV0Xdu"
    },
    {
        "author_id": "51241574",
        "created_at": "2022-12-20T02:30:08.000Z",
        "edit_history_tweet_ids": [
            "1605027744819077121"
        ],
        "id": "1605027744819077121",
        "lang": "en",
        "text": "The Air Force has grounded its entire fleet of B-2 stealth bombers following an emergency landing and fire earlier this month, and none of the strategic aircraft will perform flyovers at this years' college bowl games.  https://t.co/LuDMSWo3ll"
    }
]
```
