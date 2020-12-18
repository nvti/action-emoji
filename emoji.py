import json
import os
import re
import random
import yaml
from github import Github


def check_emoji(title):
    result = re.search("^:[a-z0-9_\+\-]+:", title)
    return result != None


def load_config():
    if os.path.isfile("./.github/emoji.yml"):
        config_file = "./.github/emoji.yml"
    elif os.path.isfile("./.github/emoji.yaml"):
        config_file = "./.github/emoji.yaml"
    else:
        return {"all": True}

    config = {
        "all": False,
        "lists": [],
        "customs": []
    }

    with open(config_file, 'r') as f:
        try:
            data = yaml.safe_load(f)
            for key in config:
                if key in data:
                    config[key] = data[key]

        except yaml.YAMLError as exc:
            print(exc)

        return config


def load_emoji():
    config = load_config()
    emojis = config['customs']
    with open("/emoji.yaml", 'r') as f:
        try:
            data = yaml.safe_load(f)
            if config['all']:
                topics = data.keys()
            else:
                topics = config['lists']

            for key, value in data.items():
                if key in topics:
                    emojis.extend(value)

        except yaml.YAMLError as exc:
            print(exc)

    if len(emojis) > 0:
        return emojis
    else:
        return ["kissing_heart"]


def get_emoji(title, emojis):
    return random.choice(emojis)


with open(os.environ["GITHUB_EVENT_PATH"]) as json_file:
    data = json.load(json_file)

g = Github(os.environ["INPUT_GITHUB_TOKEN"])
repo = g.get_repo(data['repository']['full_name'])

pull = repo.get_pull(data['pull_request']['number'])


if not check_emoji(pull.title):
    emojis = load_emoji()
    print(f"Loaded {len(emojis)} emoji")

    emoji = get_emoji(pull.title, emojis)
    print(f"Add emoji :{emoji}: to title")
    pull.edit(title=f":{emoji}: {pull.title.strip()}")
