#!/usr/bin/env bash

set -u -e -o pipefail

REPO_TEAM=''
REPO_DESC=''
REPO_NAME="$(basename "$PWD")"
REPO_README=true

function usages() {
  cat <<EOM
$(basename "$0") OPTIONS

OPTIONS:
  [-t|--team <name>]         repository team          (default: "$REPO_TEAM")
  [-d|--desc <description>]  repository description   (default: "$REPO_DESC")
  [-n|--name <name>]         repository name          (default: "$REPO_NAME")
  [-r|--readme               produce a minimal readme (default: "$REPO_README")
  [-h|--help]                shows this help message
EOM
  exit 0
}

# parse arguments
# https://stackoverflow.com/a/33826763
while [[ $# -gt 0 ]]; do
  case $1 in
  -t | --team)
    REPO_TEAM="$2"
    shift
    ;;
  -d | --desc)
    REPO_DESC="$2"
    shift
    ;;
  -n | --name)
    REPO_NAME="$2"
    shift
    ;;
  -h | --help)
    usages
    ;;
  -r | --readme)
    REPO_README="$2"
    shift
    ;;
  *)
    echo "Unknown parameter passed: $1"
    exit 1
    ;;
  esac
  shift
done

# install pre-commit
pre-commit install --install-hooks -t pre-commit -t commit-msg --overwrite
echo

if [ -z "$REPO_TEAM" ]; then
  # read a team
  TEAMS="$(grep "@DynamicYield" .github/CODEOWNERS | sed 's/^# //g')"
  COLUMNS=1
  PS3=$'\n'"Pick a team number: "
  select REPO_TEAM in $TEAMS; do break; done
else
  echo "Repository team: ${REPO_TEAM}"
fi

# define code-ownership
echo "* $REPO_TEAM" >>.github/CODEOWNERS

# define team permissions for code-ownership
REPO_TEAM_SHORT="$(echo "$REPO_TEAM" | cut -d / -f 2)"
PATCH=$(
  cat <<-EOS
teams:
  - name: $REPO_TEAM_SHORT
    permission: push
EOS
)
perl -i -p0e "s/^teams:/$PATCH/m" .github/settings.yml

if [ -z "$REPO_NAME" ]; then
  # read repository name
  read -erp "Repository name: " -i "$REPO_NAME" REPO_NAME
fi

# set repository name
perl -i -p0e "s/# name: template/name: $REPO_NAME/m" .github/settings.yml

if [ -z "$REPO_DESC" ]; then
  # read repository description
  read -erp "Repository description: " -i "$REPO_DESC" REPO_DESC
else
  echo "Repository description: ${REPO_DESC}"
fi

# set repository description
perl -i -p0e "s/description: GitHub Template Repository/description: $REPO_DESC/m" .github/settings.yml

# # delete this script
rm -f "$0"

# settings pr
git checkout main
git checkout -b settings
git add .github/settings.yml bootstrap.sh
git commit -S -m "build(repo): settings" -q
git push origin "$(git branch --show-current)"
gh pr create --base main --draft --body "# merge this first!" --title "build(repo): settings" --fill

# codeowners pr
git checkout main
git checkout -b codeowners
git add .github/CODEOWNERS
git commit -S -m "build(repo): codeowners" -q
git push origin "$(git branch --show-current)"
gh pr create --base main --draft --body "# merge this second! (after #1)" --title "build(repo): codeowners" --fill

if [ "$REPO_README" = "true" ]; then
  # readme
  cat >README.md <<EOM
# $REPO_NAME

$REPO_DESC

## Prerequisites

Describe what needs to be done for the [Getting Started](#getting-started) to work

## Getting Started

Describe what need to be done in order to work with the project

## Contributing

1. Install pre-commit

   \`\`\`shell
   pre-commit install --install-hooks -t pre-commit -t commit-msg
   \`\`\`

2. Open a pull-request

This repository was created from [template](https://github.com/DynamicYield/template)
EOM

  # readme pr
  git checkout main
  git checkout -b docs
  git add README.md
  git commit -S -m "docs(README): initial docs" -q
  git push origin "$(git branch --show-current)"
  gh pr create --base main --draft --title "docs(README): initial docs" --fill
fi

for PREFIX in DY MCD; do
  gh api '/repos/{owner}/{repo}/autolinks' \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    -f key_prefix="${PREFIX}-" \
    -f url_template="https://dynamicyield.atlassian.net/browse/${PREFIX}-<num>"
done

git checkout main
