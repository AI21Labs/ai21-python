# Contributing to AI21 Python SDK

We welcome contributions to the AI21 Python SDK. Please read the following guidelines before submitting your pull request.

### Examples of contributions include:

- Bug fixes
- Documentation improvements
- Additional tests

## Reporting issues

Go to this repository's [issues page](https://github.com/AI21Labs/ai21-python/issues) and click on the "New Issue" button.
Please make sure to check if the issue has already been reported before creating a new one.

Include the following information in your post:

- Describe what you expected to happen.
- If possible, include a [minimal reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) to help us
  identify the issue. This also helps check that the issue is not with
  your own code.
- Describe what actually happened. Include the full traceback if there
  was an exception.
- List your Python version. If possible, check if this
  issue is already fixed in the latest releases or the latest code in
  the repository.

## Submit a pull request

Fork the AI21 Python SDK repository and clone it to your local machine. Create a new branch for your changes:

    git clone https://github.com:AI21Labs/USERNAME/ai21-python
    cd ai21-python
    git checkout -b my-fix-branch master

### Installation

#### MacOS

We recommend running the provided `init.sh` script to install the required dependencies and set up the development environment. This script will install poetry if not already installed. To run the script, simply run:

    ./init.sh

#### Windows/Linux

We recommend using [poetry](https://python-poetry.org/) to install the required dependencies and set up the development environment. To install poetry, run:

    pip install poetry

Then, to install the required dependencies, run:

    poetry install

After that Install [pre-commit](https://pre-commit.com/#installation) and run:

    pre-commit install --install-hooks -t pre-commit -t commit-msg

Installing the pre-commit hooks would take care of formatting and linting your code before committing.
Please make sure you have the pre-commit hooks installed before committing your code.

**We recommend creating your own venv using pyenv or virtualenv when working on this repository, in order to eliminate unnecessary dependencies from external libraries**

### Commits

Each commit should be a single logical change and should be aligned with the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
Since we are using a pre-commit hook to enforce this, any other commit message format will be rejected.

### Run CI tasks locally

```bash
$ inv --list
Available tasks:

  clean          clean (remove) packages
  lint           python lint
  outdated       outdated packages
  test           Run unit tests
  update         update packages
  audit          run safety checks on project dependencies
  formatter      auto formats the modified files
```

### Tests

We use [pytest](https://docs.pytest.org/en/stable/) for testing. To run the tests, run:

    inv test

If adding a new test, please make sure to add it to the `tests` directory and have the file location be under the same hierarchy as the file being tested.

Make sure you use `pytest` for tests writing and not any other testing framework.

### How to open a pull request?

Push your branch to your forked repository and open a pull request against the `main` branch of the AI21 Python SDK repository. Please make sure to include a description of your changes in the pull request.

The title of the pull request should follow the above-mentioned [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

### Feedback

If you have any questions or feedback, please feel free to reach out to us.

We appreciate and encourage any contributions to the AI21 Python SDK. Please take the reviewer feedback positively and make the necessary changes to your pull request.
