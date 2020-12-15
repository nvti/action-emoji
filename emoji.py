import json
import os

with open(os.environ["GITHUB_EVENT_PATH"]) as json_file:
    data = json.load(json_file)
    print(data)
