import json
import os
import git

with open(os.environ["GITHUB_EVENT_PATH"]) as json_file:
    data = json.load(json_file)
    print(data)

g = git.cmd.Git()
g.pull()
g.checkout("origin", data['ref'])

print(g.log())
