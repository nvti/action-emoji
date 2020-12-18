import json
import os
import re
from github import Github


def check_emoji(title):
    result = re.search("^:[a-z0-9_]+:", title)
    return result != None


def get_emoji(title):
    return "jack_o_lantern"


with open(os.environ["GITHUB_EVENT_PATH"]) as json_file:
    data = json.load(json_file)

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
repo = g.get_repo(data['repository']['full_name'])

pull = repo.get_pull(data['pull_request']['number'])

if not check_emoji(pull.title):
    emoji = get_emoji(pull.title)
    print(f"Add emoji :{emoji}: to title")
    pull.edit(title=f":{emoji}: {pull.title.strip()}")
