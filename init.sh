#!/usr/bin/env bash

# create .git folder
if [[ ! -d .git ]]; then
  git init
fi

PYTHON_VERSION=$(cat .python-version)

# install the python version specified in .python-version, if not already installed
if ! pyenv versions --bare | grep -q "^${PYTHON_VERSION}"; then
  pyenv install "${PYTHON_VERSION}" --skip-existing
fi

{ [[ -d .venv ]] || {
  echo 'creating virtualenv...'
  python -m venv .venv
}; } && {
  # shellcheck disable=SC1091
  . .venv/bin/activate
} && {
  # install poetry if not already installed, or upgrade to version 2.x
  poetry_version_installed=$(poetry --version 2> /dev/null || true)
  poetry_major_version=$(echo "$poetry_version_installed" | awk '{print $3}' | cut -d '.' -f1)

  # Check if poetry_major_version is a number and if it's >= 2
  if [[ -z $poetry_version_installed || ! $poetry_major_version =~ ^[0-9]+$ || $poetry_major_version -lt 2 ]]; then
    echo "Poetry >=2 is not installed. Installing/upgrading..."
    pip install --upgrade poetry || brew install poetry
  fi
} && {
  # install keyring
  poetry self add keyrings-google-artifactregistry-auth@1.1.2
} && {
  # update lock file
  poetry lock
} && {
  # install dependencies
  poetry install --no-root && poetry sync
}

{
  # install pre-commit if not already installed
  pre-commit --version || brew install pre-commit
} && {
  # install pre-commit hooks
  pre-commit install --install-hooks -t pre-commit -t pre-push -t commit-msg
}
