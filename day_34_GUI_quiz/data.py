""" Handling Open Trivia DB API """

import requests

url    = "https://opentdb.com/api.php"
params = {
    "amount": 10,
    "type": "boolean",
}

res = requests.get(url, params=params)
res.raise_for_status()
question_data = res.json().get("results")
