"""
Habit Tracking project

API used: https://pixe.la
"""
from datetime import date, timedelta

import requests

USER_NAME = "dskarthick97"
TOKEN = "Bringmethanos@97"
CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"

# Create a user in pixela
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

create_user_res = requests.post(CREATE_USER_ENDPOINT, json=user_params)

# Create a user graph
CREATE_GRAPH_ENDPOINT = f"{CREATE_USER_ENDPOINT}/{USER_NAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Exercise - Working out Graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu",
}
headers = {"X-USER-TOKEN": TOKEN}
# create_graph_res = requests.post(
#     CREATE_GRAPH_ENDPOINT, json=graph_params, headers=headers
# )

# Post value to the graph
POST_VALUE_TO_GRAPH = f"{CREATE_GRAPH_ENDPOINT}/graph1"
today_ = date.today()
yesterday = (today_ - timedelta(days=1)).strftime("%Y%m%d")
graph_post_params = {"date": yesterday, "quantity": "120"}

create_pixel_res = requests.post(
    POST_VALUE_TO_GRAPH, json=graph_post_params, headers=headers
)
