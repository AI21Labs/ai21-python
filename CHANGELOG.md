# CHANGELOG



## v1.0.0 (2024-01-31)

### Feature

* feat: Release Candidate v2.0.0 (#26)

* ci: Change main proj name (#22)

* ci: precommit

* fix: version name

* ci: Added rc pipeline for semantic release

* ci: pypi api keys

* ci: Added rc pipeline for semantic release

* ci: pypi api keys

* fix: readme

* chore(release): v2.0.0-rc.4 [skip ci]

* docs: README.md (#23)

* ci: updated precommit hooks

* docs: more readme updates

* docs: removed extra lines

* fix: rename

* docs: readme

* docs: full readme

* docs: badges

* ci: commitizen version

* revert: via

* docs: Readme migration (#24)

* docs: instance text

* docs: client instance explanation

* ci: Remove python 3_7 support (#25)

* ci: python 3.8 &gt;= support

* ci: unittests

* test: dummy test

* docs: Readme additions (#27)

* fix: removed unnecessary url env var

* fix: README.md CR

* test: Unittests for 2.0.0 (#28)

* test: get_tokenizer tests

* fix: cases

* test: Added some unittests to resources

* fix: rename var

* test: Added ai21 studio client tsts

* fix: rename files

* fix: Added types

* test: added test to http

* fix: removed unnecessary auth param

* test: Added tests

* test: Added sagemaker

* test: Created a single session per instance

* ci: removed unnecessary action

* fix: Feedback fixes (#29)

* test: get_tokenizer tests

* fix: cases

* test: Added some unittests to resources

* fix: rename var

* test: Added ai21 studio client tsts

* fix: rename files

* fix: Added types

* test: added test to http

* fix: removed unnecessary auth param

* test: Added tests

* test: Added sagemaker

* test: Created a single session per instance

* ci: removed unnecessary action

* fix: errors

* fix: error renames

* fix: rename upload

* fix: rename type

* fix: rename variable

* fix: removed experimental

* test: fixed

* test: Added some unittests to resources

* test: Added ai21 studio client tsts

* fix: rename files

* fix: Added types

* test: added test to http

* fix: removed unnecessary auth param

* test: Added tests

* test: Added sagemaker

* test: Created a single session per instance

* fix: errors

* fix: error renames

* fix: rename upload

* fix: rename type

* fix: rename variable

* fix: removed experimental

* test: fixed

* chore(release): v2.0.0-rc.5 [skip ci]

* refactor: Add enums (#30)

* refactor: answer enum

* refactor: answer - mode enum

* refactor: moved imports

* refactor: Added enums to chat requests/response

* refactor: Added enums to completion requests/response

* fix: imports

* refactor: Added embed types enum

* refactor: Added correction type enum

* refactor: Added improvement type enum

* refactor: Added enums to paraphrase and library answer

* refactor: Added enums to segmentation

* refactor: Added enums to summary

* refactor: Added enums to summary by segment

* fix: test

* fix: bump version

* chore(release): v2.0.0-rc.6 [skip ci]

* fix: Restructure packages (#31)

* refactor: moved classes to models package

* refactor: moved responses = to models package

* refactor: moved resources to common package

* refactor: chat message rename

* refactor: init

* fix: imports

* refactor: added more to imports

* chore(release): v2.0.0-rc.7 [skip ci]

* fix: Added env config class to init (#32)

* fix: Added py.typed (#33)

* fix: Pass env config to client ctor (#34)

* fix: removed application and organization

* fix: tests

* fix: env vars to http client in sagemaker (#35)

* fix: env vars to http

* fix: env vars to http

* chore(release): v2.0.0-rc.8 [skip ci]

* fix: Removed name parameter from chat message (#36)

* fix: removed name parameter from chat message

* fix: imports in integration tests

* chore(release): v2.0.0-rc.9 [skip ci]

* fix: chat parameters (#39)

* fix: parameters for chat create

* fix: imports

* chore(release): v2.0.0-rc.10 [skip ci]

* fix: top_k_returns to top_k_return (#40)

* chore(release): v2.0.0-rc.11 [skip ci]

* fix: added user agent with more details (#42)

* test: added user agent with more details

* test: changed to capital

* test: Removed class into single tests

* ci: Add rc branch prefix trigger for integration tests (#43)

* ci: rc branch trigger for integration test

* fix: wrapped in quotes

* fix: aws tests (#44)

* ci: rc branch trigger for integration test

* fix: wrapped in quotes

* fix: AWS tests

* test: ci

* fix: AWS tests

* test: ci

* fix: Removed testing pattern for tests

* fix: Integration tests (#41)

* fix: types

* test: Added some integration tests

* test: improvements

* test: test_paraphrase.py

* fix: doc

* fix: removed unused comment

* test: test_summarize.py

* test: Added tests for test_summarize_by_segment.py

* test: test_segmentation.py

* fix: file id in library response

* fix: example for library

* ci: Add rc branch prefix trigger for integration tests (#43)

* ci: rc branch trigger for integration test

* fix: wrapped in quotes

* fix: types

* test: Added some integration tests

* test: improvements

* test: test_paraphrase.py

* fix: doc

* fix: removed unused comment

* test: test_summarize.py

* test: Added tests for test_summarize_by_segment.py

* test: test_segmentation.py

* fix: file id in library response

* fix: example for library

* docs: docstrings

* fix: question

* fix: CR

* test: Added tests to segment type in embed

* chore(deps-dev): bump jinja2 from 3.1.2 to 3.1.3 (#38)

Bumps [jinja2](https://github.com/pallets/jinja) from 3.1.2 to 3.1.3.
- [Release notes](https://github.com/pallets/jinja/releases)
- [Changelog](https://github.com/pallets/jinja/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/jinja/compare/3.1.2...3.1.3)

---
updated-dependencies:
- dependency-name: jinja2
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt;

* chore(deps-dev): bump gitpython from 3.1.40 to 3.1.41 (#37)

Bumps [gitpython](https://github.com/gitpython-developers/GitPython) from 3.1.40 to 3.1.41.
- [Release notes](https://github.com/gitpython-developers/GitPython/releases)
- [Changelog](https://github.com/gitpython-developers/GitPython/blob/main/CHANGES)
- [Commits](https://github.com/gitpython-developers/GitPython/compare/3.1.40...3.1.41)

---
updated-dependencies:
- dependency-name: gitpython
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt;

* chore(deps): bump actions/upload-artifact from 3 to 4 (#21)

Bumps [actions/upload-artifact](https://github.com/actions/upload-artifact) from 3 to 4.
- [Release notes](https://github.com/actions/upload-artifact/releases)
- [Commits](https://github.com/actions/upload-artifact/compare/v3...v4)

---
updated-dependencies:
- dependency-name: actions/upload-artifact
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt;

* chore(deps): bump pypa/gh-action-pypi-publish from 1.4.2 to 1.8.11 (#20)

Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.4.2 to 1.8.11.
- [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
- [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/27b31702a0e7fc50959f5ad993c78deac1bdfc29...2f6f737ca5f74c637829c0f5c3acd0e29ea5e8bf)

---
updated-dependencies:
- dependency-name: pypa/gh-action-pypi-publish
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt;

* chore(deps): bump actions/setup-python from 4 to 5 (#19)

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 4 to 5.
- [Release notes](https://github.com/actions/setup-python/releases)
- [Commits](https://github.com/actions/setup-python/compare/v4...v5)

---
updated-dependencies:
- dependency-name: actions/setup-python
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt;

* chore(deps): bump amannn/action-semantic-pull-request (#2)

Bumps [amannn/action-semantic-pull-request](https://github.com/amannn/action-semantic-pull-request) from 5.0.2 to 5.4.0.
- [Release notes](https://github.com/amannn/action-semantic-pull-request/releases)
- [Changelog](https://github.com/amannn/action-semantic-pull-request/blob/main/CHANGELOG.md)
- [Commits](https://github.com/amannn/action-semantic-pull-request/compare/v5.0.2...v5.4.0)

---
updated-dependencies:
- dependency-name: amannn/action-semantic-pull-request
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt;

* test: Added tests for library (#45)

* test: Added tests for library

* fix: CR

* chore(release): v2.0.0-rc.12 [skip ci]

* fix: Removed unnecessary pre commit hook

* fix: Removed autouse

* fix: CR

* docs: CONTRIBUTING.md

* docs: LICENSE

* fix: removed license

* test: Added some more unittests

---------

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: github-actions &lt;action@github.com&gt;
Co-authored-by: etang &lt;etang@ai21.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`60e3f4d`](https://github.com/AI21Labs/ai21-python/commit/60e3f4dc93f83c11ad1c1bc1f51cb64ec6036520))

### Unknown

* Update issue templates ([`c30302f`](https://github.com/AI21Labs/ai21-python/commit/c30302fd9d6dc2b0b83cea10b5a677699ea2b8a2))

* Update issue templates ([`2590685`](https://github.com/AI21Labs/ai21-python/commit/2590685fed8ea63204dcfdd47e27cb340a79cfb8))


## v2.0.0-rc.3 (2023-12-18)

### Chore

* chore(release): v2.0.0-rc.3 [skip ci] ([`0a9ace7`](https://github.com/AI21Labs/ai21-python/commit/0a9ace7dd8b59eb51b6dcb4e4a1118aaa012b454))

### Fix

* fix: Change main project name in setup (#17)

* ci: precommit

* fix: version name ([`7c68b7f`](https://github.com/AI21Labs/ai21-python/commit/7c68b7f0671681e0faab3720649760b50d05d6c6))


## v2.0.0-rc.2 (2023-12-18)

### Chore

* chore(release): v2.0.0-rc.2 [skip ci] ([`5b83506`](https://github.com/AI21Labs/ai21-python/commit/5b835060bc223bfec907624b2d717418ab51309e))

### Feature

* feat: project name (#16)

* feat: project name

* fix: name ([`e985980`](https://github.com/AI21Labs/ai21-python/commit/e98598027d955e3f0108ab1919e90195c5b2d52d))


## v2.0.0-rc.1 (2023-12-18)

### Breaking

* feat!: branch group (#15) ([`3ca1017`](https://github.com/AI21Labs/ai21-python/commit/3ca10175891ed4c51e5f4ec638eb2fd5cf05359e))

* feat!: Bump 2 rc version new (#14)

* ci: new line remove

* feat: new line ([`a086c7d`](https://github.com/AI21Labs/ai21-python/commit/a086c7d8ef40ba3f53b0144c5ba4b5911ecd5932))

### Chore

* chore(release): v1.0.0-rc.2 [skip ci] ([`ea8b6a9`](https://github.com/AI21Labs/ai21-python/commit/ea8b6a90e21f9a287a026b438ba5a5eb4eacdaa3))


## v1.0.0-rc.1 (2023-12-18)

### Breaking

* feat!: Bump 2 rc version (#13)

* docs: changelog

* docs: added text

* fix: verison ([`1426ed1`](https://github.com/AI21Labs/ai21-python/commit/1426ed16cdf9cd1d201a0bfe8bbf9a454ad685f7))

* feat!: version rc bump (#12) ([`88ccbe2`](https://github.com/AI21Labs/ai21-python/commit/88ccbe2b0d35b1f1682b0fcf58ca1a755fa26739))

* feat!: readme restart (#11) ([`992dedc`](https://github.com/AI21Labs/ai21-python/commit/992dedc63dd99dbffe78c80343afca1bb0530649))

* feat: bumping test (#10)

BREAKING CHANGE:  New SDK version

* fix: removed CHANGELOG.md

* fix: removed version rc

* fix: removed CHANGELOG.md

* fix: removed version rc ([`5650abd`](https://github.com/AI21Labs/ai21-python/commit/5650abdac34dd035b80962ce14d173376210193e))

### Chore

* chore(release): v1.0.0-rc.1 [skip ci] ([`65e09a4`](https://github.com/AI21Labs/ai21-python/commit/65e09a4146540c977c619348effcbeb443441a58))

* chore(release): v1.1.0-rc.4 [skip ci] ([`f696102`](https://github.com/AI21Labs/ai21-python/commit/f69610222200239ea8a7203d475780859c76bfab))

* chore(release): v1.1.0-rc.3 [skip ci] ([`25a4f85`](https://github.com/AI21Labs/ai21-python/commit/25a4f85a52ba024b1a44683f03ba395f8c7eb12d))

* chore(release): v1.1.0-rc.2 [skip ci] ([`d131bfc`](https://github.com/AI21Labs/ai21-python/commit/d131bfc603a3f3d1c2de32e9cd6c436169476db3))

* chore(release): v1.1.0-rc.1 [skip ci] ([`de5b2b5`](https://github.com/AI21Labs/ai21-python/commit/de5b2b55c4fb0ba99b002ec7c75c34eb130a63c8))

* chore(release): v1.10.0-rc.1 [skip ci] ([`331d142`](https://github.com/AI21Labs/ai21-python/commit/331d142e8b07c9688ab42280659a57d38759b9e6))

* chore(release): v0.1.0-rc.3 [skip ci] ([`71ee300`](https://github.com/AI21Labs/ai21-python/commit/71ee3005b92b70e1655e26566d7454c79c5008f9))

* chore(release): v0.1.0-rc.2 [skip ci] ([`46e8eae`](https://github.com/AI21Labs/ai21-python/commit/46e8eaebe8ccacafc6b90172b3c3e3da783c3d6f))

* chore(release): v0.1.0-rc.1 [skip ci] ([`3d67c2c`](https://github.com/AI21Labs/ai21-python/commit/3d67c2c9165441c09ca9a75f79021f0dba8e9325))

### Ci

* ci: python versions (#5) ([`52d18cb`](https://github.com/AI21Labs/ai21-python/commit/52d18cb6b3f4a52976aced6f24f5543886e7403f))

* ci: add_integration_test_action (#4) ([`f89e082`](https://github.com/AI21Labs/ai21-python/commit/f89e08213fc06b0328987331260368ca248f14ee))

### Feature

* feat: BREAKING CHANGE: pre release 2.0.0 (#9)

* fix: remove file

* feat: bump 1.0.0
BREAKING CHANGE: pre release ([`b15d4c7`](https://github.com/AI21Labs/ai21-python/commit/b15d4c757afe18ee000334ec8355c9baa5351505))

* feat: Test pypi (#7)

* feat: release candidate

* ci: test pypi

* fix: version ([`549d044`](https://github.com/AI21Labs/ai21-python/commit/549d0444e09e1af34b29e6d264c61bfe0c091dbe))

* feat: Pre release publish (#6)

* feat: release candidate

* fix: branch name

* fix: imports

* fix: push to test pypi ([`ed3ff91`](https://github.com/AI21Labs/ai21-python/commit/ed3ff91090f14ded7b9d1ae03fdff5ac935fbdc0))

* feat: SDK code (#3)

* feat: Added code

* feat: Added setup

* feat: more sdk code

* feat: poetry

* feat: poetry setup

* ci: actions

* fix: removed unused example

* feat: added boto3

* feat: added dependencies

* test: added pytest dependency

* fix: python version

* fix: update python version in lock

* fix: format

* fix: examples

* test: removed example script for studio and added integration test instead

* test: bedrock integration test

* test: moved examples

* ci: fixed inv

* fix: lint

* feat: version in init

* fix: long content

* fix: poetry version

* fix: added __all__

* fix: Added code to __all__

* fix: prompt

* fix: test action

* fix: Added shebang

* fix: long line

* fix: loaded env for tests

* fix: Added env

* test: only 3.10

* test: default region

* test: Added 3.8

* fix: subscriptable type

* test: sagemaker tests

* fix: used _http methods

* fix: default values

* ci: removed -vv flag

* fix: imports

* test: Added conditional skip

* fix: CR fixes

* fix: boto3 to pyproject.toml

* fix: all-extras arg

* fix: lint in action

* feat: via param

* fix: added all extras

* fix: Added static type checker

* feat: Moved body creationto function

* feat: switched most responses to use dataclasses_json

* feat: Added base mixin

* fix: CR

* fix: test path

* fix: CR

* feat: Added bedrock session

* feat: Added SageMakerSession

* fix: init of bedrock client

* feat: More robust imports

* fix: error message

* fix: removed kwargs from request body

* fix: Removed log_level from env

* fix: logger calls

* fix: Removed logger from init

* feat: Added setup logger

* ci: Added integration tests only on push to main

* fix: removed unused import ([`0e9b36a`](https://github.com/AI21Labs/ai21-python/commit/0e9b36aca7ab0a3800552c8929c6f4f7d1cd9e1f))

### Fix

* fix: test pypi params (#8) ([`ed8fa1f`](https://github.com/AI21Labs/ai21-python/commit/ed8fa1f7b52b0ab6f94ed9815adf0256152dd02e))

### Unknown

* Initial commit ([`a2841de`](https://github.com/AI21Labs/ai21-python/commit/a2841dead1d9324d444fded170b64d280fef3394))
