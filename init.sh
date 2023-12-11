#!/bin/bash

cd "$(dirname "$0")" || exit

# create .git folder
if [[ ! -d .git ]]; then
  git init
fi

# install the python version specified in .python-version, if not already installed
if pyenv --version; then
  pyenv install --skip-existing
fi

# install poetry if not already installed
if ! poetry --version; then
  brew install poetry
fi

# poetry needs to create the venv with the same python version
poetry env use "$(cat .python-version)"

# update lock file
poetry lock --no-update

# install dependencies
poetry install

# install pre-commit if not already installed
if ! pre-commit --version; then
  brew install pre-commit
fi

# install pre-commit hooks
pre-commit install --install-hooks -t pre-commit -t commit-msg

# shellcheck source=/dev/null
source .venv/bin/activate
