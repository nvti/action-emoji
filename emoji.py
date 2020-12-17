import json
import os
import re
from github import Github


def check_emoji(title):
    result = re.search("^:[a-z0-9_]+:", title)
    print(result)
    return result != None


with open(os.environ["GITHUB_EVENT_PATH"]) as json_file:
    data = json.load(json_file)
    print(data)

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
repo = g.get_repo(data['repository']['full_name'])

pull = repo.get_pull(data['pull_request']['number'])

if not check_emoji(pull.title):
    pull.edit(title=":jack_o_lantern: " + pull.title.trim())
