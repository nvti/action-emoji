import json
import os
import re
import random
import yaml
from github import Github


def check_emoji(title):
    result = re.search("^:[a-z0-9_\+\-]+:", title)
    return result != None


def load_emoji():
    emojis = []
    with open("/emoji.yaml", 'r') as f:
        try:
            data = yaml.safe_load(f)
            for _, value in data.items():
                emojis.extend(value)

            return emojis

        except yaml.YAMLError as exc:
            print(exc)
            return ["kissing_heart"]


def get_emoji(title, emojis):
    return random.choice(emojis)


with open(os.environ["GITHUB_EVENT_PATH"]) as json_file:
    data = json.load(json_file)

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
repo = g.get_repo(data['repository']['full_name'])

pull = repo.get_pull(data['pull_request']['number'])

emojis = load_emoji()
print(f"Loaded {len(emojis)} emoji")

if not check_emoji(pull.title):
    emoji = get_emoji(pull.title, emojis)
    print(f"Add emoji :{emoji}: to title")
    pull.edit(title=f":{emoji}: {pull.title.strip()}")
