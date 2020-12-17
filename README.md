# Emoji commit

This is a fun github action, to add random emoji to every commit message 🚀💖

## Inputs

### GITHUB_TOKEN

**Required** In order for GitHub to trigger the rebuild of your page you must provide the action with the repositories provided GitHub token.

## Example

```yml
name: Add Emoji
on:
  push:
    branches:
      - "master"
jobs:
  add-emoji:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout 🛎️
        uses: actions/checkout@v2

      - name: Add emoji 🥰
        uses: tiena2cva/action-emoji@v0.5
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
