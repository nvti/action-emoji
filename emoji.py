import json
import os
from github import Github

with open(os.environ["GITHUB_EVENT_PATH"]) as json_file:
    data = json.load(json_file)
    print(data)

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
print(g)
