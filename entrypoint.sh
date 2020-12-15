#!/bin/bash -eu

_main() {
    _switch_to_repository

    _switch_to_branch

    _add_files

    _local_commit

    _tag_commit

    _push_to_github
}

_switch_to_repository() {
    echo "INPUT_REPOSITORY value: $INPUT_REPOSITORY";
    cd "$INPUT_REPOSITORY";
}

_switch_to_branch() {
    echo "INPUT_BRANCH value: $INPUT_BRANCH";

    # Fetch remote to make sure that repo can be switched to the right branch.
    git fetch;

    # Switch to branch from current Workflow run
    git checkout $INPUT_BRANCH;
}

_config_git() {
    echo "INPUT_COMMIT_USER_NAME: ${INPUT_COMMIT_USER_NAME}";
    echo "INPUT_COMMIT_USER_EMAIL: ${INPUT_COMMIT_USER_EMAIL}";
    echo "INPUT_COMMIT_AUTHOR: ${INPUT_COMMIT_AUTHOR}";
}

printenv

cat ${GITHUB_EVENT_PATH}
