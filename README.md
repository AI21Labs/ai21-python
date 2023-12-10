# Git Repository Template

[Template](https://github.com/DynamicYield/template) is a [*Git repository template*](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) for bootstrapping your repositories.

Bundled support for:

- [Code Owners](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-code-owners#about-code-owners) — Automatically requested for review when someone opens a pull request that modifies code that they own as defined in [`.github/CODEOWNERS`](.github/CODEOWNERS)

  - The first thing you should do, is **set a [team](https://github.com/AI21/template/blob/main/.github/CODEOWNERS) as a code owner for the `.github/settings.yml`**.

- [ProBot Settings](https://github.com/probot/settings) — Synchronize repository settings defined in [`.github/settings.yml`](.github/settings.yml) to GitHub, enabling Pull Requests for repository settings

  When adding/removing/modifying jobs within workflows, you might need to tweak the *required status checks* in this file; the required status checks must pass before you can merge your branch into the protected branch.

- [ProBot Stale](https://github.com/probot/stale/) — Closes abandoned Issues and Pull Requests after a period of inactivity as defined in [`.github/stale.yml`](.github/stale.yml)
- [DependaBot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates) — Alerts on security vulnerabilities within the repository's dependencies, and updates the dependencies automatically as defined in [`.github/dependabot.yml`](.github/dependabot.yml)
- [RenovateBot](https://github.com/renovatebot/renovate) — Universal dependency update tool as defined in [`.github/renovate.json`](.github/renovate.json) ([application dashboard](https://app.renovatebot.com))
- [Pre-commit](https://pre-commit.com/) — Managing and maintaining multi-language pre-commit hooks as defined in [`.pre-commit-config.yaml`](.pre-commit-config.yaml)

  - Leverage `pre-commit` to [install the Git hooks](https://pre-commit.com/#pre-commit-install)

    ```shell
    pre-commit install --install-hooks -t pre-commit -t commit-msg
    ```

  - You can check which files `pre-commit` works on by running

    ```shell
    pre-commit run list-files --hook-stage manual --verbose
    ```

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) — An easy set of rules for creating an explicit commit history; which makes it easier to write automated tools on top of. Such as generating a [changelog](https://keepachangelog.com/)

  ```shell
  git cz changelog
  ```

---

## Automation Features

We **strongly recommend** to enable the following features manually

### Code review assignment

[Code review assignments clearly indicate which members of a team are expected to submit a review for a pull request](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-code-review-assignment-for-your-team).

### Scheduled reminders

You can get reminders in Slack when your [team has pull requests waiting for review](https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team#creating-a-scheduled-reminder-for-a-team) or for [your user with real-time alerts](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-your-membership-in-organizations/managing-your-scheduled-reminders).

## Prerequisites

We are using a collection of tools. In order to work with this repository please [configure your Mac](https://github.com/AI21/dev-envs#getting-started)

## Quick Start

Run [`./bootstrap.sh`](./bootstrap.sh) and follow the interactive on-screen instructions. For more information, Run `./bootstrap.sh --help`.

This will install pre-commit hooks, modify relevant files, deletes itself and open a draft pull-request.

## Syncing with the Template repository

To keep your repository up-to-date with the template git repository, execute the following from within your repository's root directory

```shell
git clone git@github.com:AI21/template.git ../template
git checkout -b template-sync
rsync -ax --exclude .git --exclude README.md --exclude CHANGELOG.md --exclude bootstrap.sh ../template/ .
```

Then do cherry-picking for the changes which you would like to merge.

---

## Modify this README to suit the project
