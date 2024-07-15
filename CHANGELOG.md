# CHANGELOG

## v2.9.2 (2024-07-15)

### Fix

* fix: fix default for require_api_key in http client and other clients (#185)

* fix: fix default for require_api_key in http client and other clients

* test: fix unittests

* test: add ai21 azure client ([`e6b305e`](https://github.com/AI21Labs/ai21-python/commit/e6b305edc8ed36c722cc359f499c764e05248b95))

## v2.9.1 (2024-07-10)

### Chore

* chore(release): v2.9.1 [skip ci] ([`5ed7f07`](https://github.com/AI21Labs/ai21-python/commit/5ed7f07e677ce60eb960991f3c601869d4e2c68c))

* chore(deps-dev): bump zipp from 3.18.1 to 3.19.1 (#183)

Bumps [zipp](https://github.com/jaraco/zipp) from 3.18.1 to 3.19.1.
- [Release notes](https://github.com/jaraco/zipp/releases)
- [Changelog](https://github.com/jaraco/zipp/blob/main/NEWS.rst)
- [Commits](https://github.com/jaraco/zipp/compare/v3.18.1...v3.19.1)

---
updated-dependencies:
- dependency-name: zipp
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`1812ef5`](https://github.com/AI21Labs/ai21-python/commit/1812ef50f3700bc994694c9b45a7c1cf51c45f87))

* chore(deps): bump certifi from 2024.2.2 to 2024.7.4 (#176)

Bumps [certifi](https://github.com/certifi/python-certifi) from 2024.2.2 to 2024.7.4.
- [Commits](https://github.com/certifi/python-certifi/compare/2024.02.02...2024.07.04)

---
updated-dependencies:
- dependency-name: certifi
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`f5e1814`](https://github.com/AI21Labs/ai21-python/commit/f5e18140ffd289be8d3e5afa2e0c5352a0beb1cd))

* chore(deps): bump amannn/action-semantic-pull-request (#154)

Bumps [amannn/action-semantic-pull-request](https://github.com/amannn/action-semantic-pull-request) from 5.5.2 to 5.5.3.
- [Release notes](https://github.com/amannn/action-semantic-pull-request/releases)
- [Changelog](https://github.com/amannn/action-semantic-pull-request/blob/main/CHANGELOG.md)
- [Commits](https://github.com/amannn/action-semantic-pull-request/compare/v5.5.2...v5.5.3)

---
updated-dependencies:
- dependency-name: amannn/action-semantic-pull-request
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`e57d99a`](https://github.com/AI21Labs/ai21-python/commit/e57d99a04ff4b6aa4a858a2fe87f8cc8c68bcfa0))

### Fix

* fix: remove httpx logger on log level info (#184) ([`06d0226`](https://github.com/AI21Labs/ai21-python/commit/06d02261c187a4bda1b5d479855d17b5a1507a1d))

### Unknown

* Securely use variables in labeler workflow. (#181)

Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`5349992`](https://github.com/AI21Labs/ai21-python/commit/53499926753a1854a2da6c65f8175c33d0a79ae1))

## v2.9.0 (2024-07-07)

### Chore

* chore(release): v2.9.0 [skip ci] ([`f4b4d36`](https://github.com/AI21Labs/ai21-python/commit/f4b4d362b77ab94c970ae623f7f9185b94718181))

* chore(deps): bump actions/github-script from 6 to 7 (#169)

Bumps [actions/github-script](https://github.com/actions/github-script) from 6 to 7.
- [Release notes](https://github.com/actions/github-script/releases)
- [Commits](https://github.com/actions/github-script/compare/v6...v7)

---
updated-dependencies:
- dependency-name: actions/github-script
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`de4b1af`](https://github.com/AI21Labs/ai21-python/commit/de4b1af5654b30fbf01d7258a9174eb091362b1d))

* chore: semantic pr - allow running on external prs (#164) ([`032fd5d`](https://github.com/AI21Labs/ai21-python/commit/032fd5d3a384f8dba26568c0b618e7c5f59a0431))

* chore: add status report to integration workflow (#161)

* chore: add status report to integration workflow

* chore: add status report to integration workflow lint

* chore: export lint to separate workflow ([`0a3a1e0`](https://github.com/AI21Labs/ai21-python/commit/0a3a1e02a6e44ac6589ff18e19c03c8cf5d94c19))

* chore: integration-tests.yaml update inputs (#160) ([`b3f7728`](https://github.com/AI21Labs/ai21-python/commit/b3f772859374303efc130083d0f0aba0b1743398))

* chore: integration-tests.yaml update inputs (#159) ([`f61c905`](https://github.com/AI21Labs/ai21-python/commit/f61c9059ecb6cc8c4fafdec7f86205a768976f32))

* chore: integration-tests.yaml update checkout to specific commit (#158) ([`1c01663`](https://github.com/AI21Labs/ai21-python/commit/1c016630428085c44a6b1437fa87831a6b684fcb))

* chore: Update testing workflows (#156)

* chore: change triggers for workflows tests, integration-tests

* chore: integration-tests.yaml - add trigger for push on main ([`4c170b8`](https://github.com/AI21Labs/ai21-python/commit/4c170b8378e6bfe06a1bc342d612ad1711792fca))

### Ci

* ci: Update size label When PR size changes (#171) (#172)

* ci: Update size label

* test: File to test label

* fix: Remove file ([`6dd535a`](https://github.com/AI21Labs/ai21-python/commit/6dd535a4da3959ea258a2d316be7c145961b6875))

* ci: remove explicit permissions from semantic-pr.yml (#167) ([`3674efc`](https://github.com/AI21Labs/ai21-python/commit/3674efc106959f9b5b9b35c6eacc19db413c80cf))

### Feature

* feat: Async Support AWS (#180)

* feat: Add bedrock async support (#146)

* refactor: migrate from boto3 to custom http client

* refactor: create an aws http client, and switch bedrock client to use it

* test: rename test, add async tests

* feat: add async client, remove bedrock_session class

* docs: Azure README (#139)

* feat: Add async tokenizer, add detokenize method (#144)

* feat: add detokenize method, add async tokenizer

* chore: update pyproject and poetry.lock

* fix: fix tokenizer name in examples and readme, add example

* test: adjust unittest + add unittest for async

* chore: cache -&gt; lru_cache to support python 3.8

* test: fix test_imports test

* chore: add env_config to bedrock client to avoid breaking changes

* refactor: export aws auth logic to new class

* refactor: remove aws_http_client, use http_client instead, add aws auth test

* test: fix tests

* refactor: remove aws_http_client

* chore(deps-dev): bump authlib from 1.3.0 to 1.3.1 (#131)

Bumps [authlib](https://github.com/lepture/authlib) from 1.3.0 to 1.3.1.
- [Release notes](https://github.com/lepture/authlib/releases)
- [Changelog](https://github.com/lepture/authlib/blob/master/docs/changelog.rst)
- [Commits](https://github.com/lepture/authlib/compare/v1.3.0...v1.3.1)

---
updated-dependencies:
- dependency-name: authlib
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt;

* chore(deps): bump pypa/gh-action-pypi-publish from 1.8.14 to 1.9.0 (#138)

Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.8.14 to 1.9.0.
- [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
- [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/81e9d935c883d0b210363ab89cf05f3894778450...ec4db0b4ddc65acdf4bff5fa45ac92d78b56bdf0)

---
updated-dependencies:
- dependency-name: pypa/gh-action-pypi-publish
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt;

* chore: rebase code

* refactor: chat + chat completions - migrate to new client

* refactor: cr comments

* chore: add async to new bedrock components

* refactor: rename aws folder

* chore: fix typo on file name bedrock_chat_completions

* fix: fix errors

* chore: fix typo

* fix: Added deprecation warning

* fix: Added deprecation warning to async

* chore: add log for ignoring stream

---------

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;

* Add sagemaker async support (#155)

* refactor: migrate from boto3 to custom http client

* refactor: create an aws http client, and switch bedrock client to use it

* test: rename test, add async tests

* feat: add async client, remove bedrock_session class

* docs: Azure README (#139)

* feat: Add async tokenizer, add detokenize method (#144)

* feat: add detokenize method, add async tokenizer

* chore: update pyproject and poetry.lock

* fix: fix tokenizer name in examples and readme, add example

* test: adjust unittest + add unittest for async

* chore: cache -&gt; lru_cache to support python 3.8

* test: fix test_imports test

* chore: add env_config to bedrock client to avoid breaking changes

* refactor: sagemaker client, boto-&gt;aws http client

* refactor: export aws auth logic to new class

* refactor: remove aws_http_client, use http_client instead, add aws auth test

* test: fix tests

* refactor: remove aws_http_client

* chore(deps-dev): bump authlib from 1.3.0 to 1.3.1 (#131)

Bumps [authlib](https://github.com/lepture/authlib) from 1.3.0 to 1.3.1.
- [Release notes](https://github.com/lepture/authlib/releases)
- [Changelog](https://github.com/lepture/authlib/blob/master/docs/changelog.rst)
- [Commits](https://github.com/lepture/authlib/compare/v1.3.0...v1.3.1)

---
updated-dependencies:
- dependency-name: authlib
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt;

* chore(deps): bump pypa/gh-action-pypi-publish from 1.8.14 to 1.9.0 (#138)

Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.8.14 to 1.9.0.
- [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
- [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/81e9d935c883d0b210363ab89cf05f3894778450...ec4db0b4ddc65acdf4bff5fa45ac92d78b56bdf0)

---
updated-dependencies:
- dependency-name: pypa/gh-action-pypi-publish
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt;

* chore: rebase code

* refactor: chat + chat completions - migrate to new client

* refactor: cr comments

* chore: add async to new bedrock components

* refactor: rename aws folder

* chore: refactor to use http client

* chore: fix typo on file name bedrock_chat_completions

* fix: fix errors

* chore: fix typo

* chore: add async to sm resources

* test: fix imports test

* fix: Added deprecation warning

* fix: Added deprecation warning to async

* chore: add log for ignoring stream

* chore: fix lint

* refactor: export get_aws_region, add async sm to readme, add async examples

* test: add async test files to test_sagemaker.py

* refactor: remove get_aws_region func

---------

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;

* feat: Use the same http client for all Clients (#163)

* fix: Merge

* feat: AI21Client to inherit from AI21HTTPClient

* feat: Used RequestOptions class

* fix: api error

* fix: Rename update to replace

* fix: Tests

* test: Added bedrock tests

* fix: Added support for model and model_id for backwards compatibility

* fix: Deprecation warning message

* fix: Added ANY to dict

* fix: Removed redundant code

* fix: base_url

* fix: Added deprecation warning

* fix: Moved &#39;model&#39; extract

* test: Added a tests to validate model_id and model cant be together

* fix: Test

* fix: Bedrock integration tests

---------

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: miri-bar &lt;160584887+miri-bar@users.noreply.github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`5248d96`](https://github.com/AI21Labs/ai21-python/commit/5248d96a783b5ffab7cb7c9f6de383a1eba4df11))

* feat: Added Log Verbosity (#152)

* fix: Added logger to httpx

* feat: Added set_verbose

* feat: Added set_debug

* fix: api-key header

* fix: Removed unused function

* feat: Logged env variables

* fix: Changed call location

* fix: CR

* fix: Added amazon header to secrets ([`57b1ea9`](https://github.com/AI21Labs/ai21-python/commit/57b1ea9aa172fdef7723199fe77ca50a15d6427c))

### Fix

* fix: label parse (#178) ([`1ea52f5`](https://github.com/AI21Labs/ai21-python/commit/1ea52f5b7b842edcb6f61e40edc9c8c58e49d9ac))

* fix: rest call (#174) ([`24caf96`](https://github.com/AI21Labs/ai21-python/commit/24caf96a291a33b51df77a1ca1223eca639d741b))

* fix: Version of action and json parser (#173) ([`8a270ec`](https://github.com/AI21Labs/ai21-python/commit/8a270ecfc3e8b5d312dbe49d2a47a41c31be9be3))

## v2.8.0 (2024-06-26)

### Chore

* chore(release): v2.8.0 [skip ci] ([`c5087cf`](https://github.com/AI21Labs/ai21-python/commit/c5087cf6f20accdeba57d7630e1cd780de36e435))

* chore(deps): bump python-semantic-release/python-semantic-release (#143)

Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.8.0 to 9.8.3.
- [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.0...v9.8.3)

---
updated-dependencies:
- dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`718baaa`](https://github.com/AI21Labs/ai21-python/commit/718baaacce4af67c39c6e875782948e2158f22d4))

* chore(deps): bump urllib3 from 1.26.18 to 1.26.19 (#140)

Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.18 to 1.26.19.
- [Release notes](https://github.com/urllib3/urllib3/releases)
- [Changelog](https://github.com/urllib3/urllib3/blob/1.26.19/CHANGES.rst)
- [Commits](https://github.com/urllib3/urllib3/compare/1.26.18...1.26.19)

---
updated-dependencies:
- dependency-name: urllib3
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`dccf911`](https://github.com/AI21Labs/ai21-python/commit/dccf9117a2b17a74f8e9c298de22a072b84c6994))

### Ci

* ci: Update pull request action (#151) ([`bf535c6`](https://github.com/AI21Labs/ai21-python/commit/bf535c64a71a17d257dadbdfbe7ef5c384b1268a))

### Documentation

* docs: update README.md (#149)

minor fix

Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`09798b1`](https://github.com/AI21Labs/ai21-python/commit/09798b1e730098d0f3d43695a39d416a75f5a17d))

* docs: Fix message pass (#150) ([`8f41631`](https://github.com/AI21Labs/ai21-python/commit/8f41631025021f19b665c0b4836a664438957549))

### Feature

* feat: adding Jamaba-Instruct-V1(chat_completions) to AWS Bedrock (#153)

* feat: adding Jamaba-Instruct-V1(chat_completions) to AWS Bedrock

* feat: adding integration tests to bedrock chat completions + update README.md

* fix: Semantics

* fix: README order of bullets

* docs: Updated README.md

* docs: Added -U

* fix: Handle error message

---------

Co-authored-by: Josephasafg &lt;ajgard7@gmail.com&gt; ([`7fae5c6`](https://github.com/AI21Labs/ai21-python/commit/7fae5c6dd097ee491ed3a37c6c0b1b2e6f21502a))

## v2.7.0 (2024-06-21)

### Chore

* chore(release): v2.7.0 [skip ci] ([`054459e`](https://github.com/AI21Labs/ai21-python/commit/054459e1289efb1a82a81a37038c7ca32279f5ed))

* chore(deps): bump pypa/gh-action-pypi-publish from 1.8.14 to 1.9.0 (#138)

Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.8.14 to 1.9.0.
- [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
- [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/81e9d935c883d0b210363ab89cf05f3894778450...ec4db0b4ddc65acdf4bff5fa45ac92d78b56bdf0)

---
updated-dependencies:
- dependency-name: pypa/gh-action-pypi-publish
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`c509b7e`](https://github.com/AI21Labs/ai21-python/commit/c509b7e59aa984cc9948db1362162eaa52eeb1d7))

* chore(deps-dev): bump authlib from 1.3.0 to 1.3.1 (#131)

Bumps [authlib](https://github.com/lepture/authlib) from 1.3.0 to 1.3.1.
- [Release notes](https://github.com/lepture/authlib/releases)
- [Changelog](https://github.com/lepture/authlib/blob/master/docs/changelog.rst)
- [Commits](https://github.com/lepture/authlib/compare/v1.3.0...v1.3.1)

---
updated-dependencies:
- dependency-name: authlib
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`5eeaf52`](https://github.com/AI21Labs/ai21-python/commit/5eeaf52af19eee54d19fb9430b6caadf972e5f9c))

### Ci

* ci: Added parter labels (#147) ([`737d98f`](https://github.com/AI21Labs/ai21-python/commit/737d98f0b28d6e335b747dbae44fc68929cf39d6))

* ci: Auto Label (#142)

* ci: Auto lgtm

* fix: script

* fix: consts

* ci: Auto labeler action

* fix: on

* fix: Added more triggers

* fix: feat trigger

* ci: size labels

* fix: More tests

* docs: remove to add

* docs: Updated labeler

* fix: Added default

* fix: Removed line

* fix: labeler

* fix: prints

* fix: Script

* fix: scri[pt

* ci: Added prints

* ci: More prints

* ci: Added echo 0

* ci: Fixed condition

* fix: condition

* fix: Removed unused lines

* fix: Removed more prints

* ci: Lgtm

* fix: condition ([`b59407c`](https://github.com/AI21Labs/ai21-python/commit/b59407cb44e0f13ddc85cb07e721126df5acccfb))

### Documentation

* docs: Azure README (#139) ([`5b0eadb`](https://github.com/AI21Labs/ai21-python/commit/5b0eadbe88702e2ca28de608191d9a17b8c0b4b0))

### Feature

* feat: Add async tokenizer, add detokenize method (#144)

* feat: add detokenize method, add async tokenizer

* chore: update pyproject and poetry.lock

* fix: fix tokenizer name in examples and readme, add example ([`f2d06fc`](https://github.com/AI21Labs/ai21-python/commit/f2d06fc7d2bc155beeaec72c0481f9a239656c07))

### Fix

* fix: Add default version to azure url (#148)

* fix: Added azure api version in the url

* fix: Added _create_base_url ([`cbea1d1`](https://github.com/AI21Labs/ai21-python/commit/cbea1d19197bf48c26679f8f97d37013333994f6))

## v2.6.0 (2024-06-13)

### Chore

* chore(release): v2.6.0 [skip ci] ([`3a6de49`](https://github.com/AI21Labs/ai21-python/commit/3a6de495aa88dc98577b8b27fff94cb88d7662ba))

### Feature

* feat: Azure Client Support (#135) ([`6115632`](https://github.com/AI21Labs/ai21-python/commit/611563279999168703e49dbbf288190ee0ae262d))

## v2.5.2 (2024-06-13)

### Chore

* chore(release): v2.5.2 [skip ci] ([`3eae31e`](https://github.com/AI21Labs/ai21-python/commit/3eae31e1f82cec6bcf208d1ed614daa0fd6ddad1))

### Fix

* fix: camel case (#136) ([`e2b8466`](https://github.com/AI21Labs/ai21-python/commit/e2b846666bf5b2b8617cc26214fa5f36d65f5e35))

## v2.5.1 (2024-06-13)

### Chore

* chore(release): v2.5.1 [skip ci] ([`e2a43b8`](https://github.com/AI21Labs/ai21-python/commit/e2a43b82cf891d8858d8927be77e696ff9ace4b3))

### Fix

* fix: Chain /studio/v1 to default url (#134)

* fix: Chain /studio/v1

* fix: Async Client

* fix: Support urls

* fix: Extra line

* fix: Moved to external function ([`8d305c5`](https://github.com/AI21Labs/ai21-python/commit/8d305c537df846be8f6c12ba0e165c6d8ae3c06d))

## v2.5.0 (2024-06-10)

### Chore

* chore(release): v2.5.0 [skip ci] ([`f829c8f`](https://github.com/AI21Labs/ai21-python/commit/f829c8fc5430d65e771931c8c1f0af09bd75f94e))

### Feature

* feat: add support for studio async client (#129)

* feat: async support - stream, http, ai21 http

* fix: commit changes

* feat: studio resource, chat, chat completions, answer

* feat: beta, dataset, completion, custom model

* feat: embed, gec, improvements

* feat: paraphrase, segmentation, summarize, by segment

* feat: library

* feat: client

* refactor: sync and async http, ai21 http, ai21 client, resources

* test: update imports, create tests for async

* fix: base client

* fix: add pytest marker asyncio

* fix: add pytest asyncio to poetry

* fix: add delete to lib files, add examples, test examples

* fix: tests

* fix: fix stream, add stream tests, add readme

* fix: fix import on sm stub

* feat: async support - stream, http, ai21 http

* fix: commit changes

* feat: studio resource, chat, chat completions, answer

* feat: beta, dataset, completion, custom model

* feat: embed, gec, improvements

* feat: paraphrase, segmentation, summarize, by segment

* feat: library

* feat: client

* refactor: sync and async http, ai21 http, ai21 client, resources

* test: update imports, create tests for async

* fix: base client

* fix: add pytest marker asyncio

* fix: add pytest asyncio to poetry

* fix: add delete to lib files, add examples, test examples

* fix: tests

* fix: fix stream, add stream tests, add readme

* fix: fix import on sm stub

* fix: fix async http client, fix tests

* fix: remove commented out code

* fix: CR comments

* fix: fix failing test

* fix: fix failing test

* fix: fix failing test

* fix: fix library test

* fix: cr comments ([`d1933e4`](https://github.com/AI21Labs/ai21-python/commit/d1933e4f4ba5964c4622b737504fbd0f0f77353a))

### Fix

* fix: Pass Base URL to HTTP Client (#128)

* fix: Support base urls

* fix: tests ([`8b91187`](https://github.com/AI21Labs/ai21-python/commit/8b9118746bc30c9ba91fbca80ca6c6a9256d2876))

## v2.4.2 (2024-06-06)

### Chore

* chore(release): v2.4.2 [skip ci] ([`15109d6`](https://github.com/AI21Labs/ai21-python/commit/15109d6d1747c939612fa1a546818d011283e6ea))

### Fix

* fix: parameters (#130) ([`dfcc567`](https://github.com/AI21Labs/ai21-python/commit/dfcc5675dc22fc3aafe7624b7e8ebd8cbd021146))

## v2.4.1 (2024-06-03)

### Chore

* chore(release): v2.4.1 [skip ci] ([`f708889`](https://github.com/AI21Labs/ai21-python/commit/f708889469a022a26df4dcd2dc29636cebc5f581))

* chore(deps): bump python-semantic-release/python-semantic-release (#121)

Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.7.3 to 9.8.0.
- [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.7.3...v9.8.0)

---
updated-dependencies:
- dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`c8ade60`](https://github.com/AI21Labs/ai21-python/commit/c8ade60602661e0193e33371e942dd7a4600915a))

### Ci

* ci: Added reach for auto assign (#124) ([`3f3aed0`](https://github.com/AI21Labs/ai21-python/commit/3f3aed0a653aef7a5addc005e96323c5f8874108))

### Fix

* fix: num_retries (#125) ([`cbbc213`](https://github.com/AI21Labs/ai21-python/commit/cbbc213bd840158797d3b5cfbcbc11200bd12f06))

### Unknown

* --- (#118)

updated-dependencies:
- dependency-name: requests
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`30e1e58`](https://github.com/AI21Labs/ai21-python/commit/30e1e589e050958d277af00dd2aadbc493b9c56d))

## v2.4.0 (2024-05-28)

### Chore

* chore(release): v2.4.0 [skip ci] ([`b4062d2`](https://github.com/AI21Labs/ai21-python/commit/b4062d250f04b89b0f9ddd6762d61dd1363f0dc5))

### Feature

* feat: Added beta to client (#123) ([`e3bfb27`](https://github.com/AI21Labs/ai21-python/commit/e3bfb272fc2d5f4341dff55d90e34da319b464f1))

### Fix

* fix: Update library_search_response.py (#122)

feat: adding new field: order to library-search api response

Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`c8b57a8`](https://github.com/AI21Labs/ai21-python/commit/c8b57a8177754a376d2f53e2f730682832e76f04))

## v2.3.1 (2024-05-22)

### Chore

* chore(release): v2.3.1 [skip ci] ([`b6d3186`](https://github.com/AI21Labs/ai21-python/commit/b6d3186a3854a2f04366558f17f5b2d81cd88fdc))

* chore(deps): bump idna from 3.6 to 3.7 (#96)

Bumps [idna](https://github.com/kjd/idna) from 3.6 to 3.7.
- [Release notes](https://github.com/kjd/idna/releases)
- [Changelog](https://github.com/kjd/idna/blob/master/HISTORY.rst)
- [Commits](https://github.com/kjd/idna/compare/v3.6...v3.7)

---
updated-dependencies:
- dependency-name: idna
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`7c52f19`](https://github.com/AI21Labs/ai21-python/commit/7c52f19012d400a23e38f5e41191d5f865c7d0a6))

### Documentation

* docs: Table of contents in readme (#119)

* docs: Updated docs with table of contents

* fix: docs

* fix: more docs stuff

* fix: emoji

* fix: cloud emoji ([`aca280e`](https://github.com/AI21Labs/ai21-python/commit/aca280e3d57f70c054491fbcaee45a905dda6b6b))

### Fix

* fix: updated env var in real time (#120) ([`d19332d`](https://github.com/AI21Labs/ai21-python/commit/d19332d43d138b2060670561abbac292ece76826))

## v2.3.0 (2024-05-20)

### Chore

* chore(release): v2.3.0 [skip ci] ([`d2d416a`](https://github.com/AI21Labs/ai21-python/commit/d2d416aaaf018c9905ad947fe70e30dfd951b5e6))

* chore(deps): bump python-semantic-release/python-semantic-release (#115)

Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.3.1 to 9.7.3.
- [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.3.1...v9.7.3)

---
updated-dependencies:
- dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`2ff5912`](https://github.com/AI21Labs/ai21-python/commit/2ff5912c38be61ea3c06b52037109eb7504ae1a2))

* chore(deps): bump amannn/action-semantic-pull-request (#103)

Bumps [amannn/action-semantic-pull-request](https://github.com/amannn/action-semantic-pull-request) from 5.4.0 to 5.5.2.
- [Release notes](https://github.com/amannn/action-semantic-pull-request/releases)
- [Changelog](https://github.com/amannn/action-semantic-pull-request/blob/main/CHANGELOG.md)
- [Commits](https://github.com/amannn/action-semantic-pull-request/compare/v5.4.0...v5.5.2)

---
updated-dependencies:
- dependency-name: amannn/action-semantic-pull-request
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Joseph Gardin &lt;39553475+Josephasafg@users.noreply.github.com&gt; ([`5dd95ac`](https://github.com/AI21Labs/ai21-python/commit/5dd95acdeb73967377ada7ba3da98002df58398f))

### Feature

* feat: Jamba Stream Support (#117)

* feat: Add httpx support (#111)

* feat: Added httpx to pyproject

* feat: httpx instead of requests

* feat: Removed requests

* fix: not given

* fix: setup

* feat: Added tenacity for retry

* fix: conftest

* test: Added tests

* fix: Rename

* fix: Modified test

* fix: CR

* fix: request

* feat: Stream support jamba (#114)

* feat: Added httpx to pyproject

* feat: httpx instead of requests

* feat: Removed requests

* fix: not given

* fix: setup

* feat: Added tenacity for retry

* fix: conftest

* test: Added tests

* fix: Rename

* fix: Modified test

* feat: stream support (unfinished)

* feat: Added tenacity for retry

* test: Added tests

* fix: Rename

* feat: stream support (unfinished)

* fix: single request creation

* feat: Support stream_cls

* fix: passed response_cls

* fix: Removed unnecessary json_to_response

* fix: imports

* fix: tests

* fix: imports

* fix: reponse parse

* fix: Added two examples to tests

* fix: sagemaker tests

* test: Added stream tests

* fix: comment out failing test

* fix: CR

* fix: Removed code

* docs: Added readme for streaming

* fix: condition

* docs: readme

* test: Added integration test for streaming

* fix: Added enter and close to stream

* fix: Uncomment chat completions test

* feat: Add httpx support (#111)

* feat: Added httpx to pyproject

* feat: httpx instead of requests

* feat: Removed requests

* fix: not given

* fix: setup

* feat: Added tenacity for retry

* fix: conftest

* test: Added tests

* fix: Rename

* fix: Modified test

* fix: CR

* fix: request

* feat: Stream support jamba (#114)

* feat: Added httpx to pyproject

* feat: httpx instead of requests

* feat: Removed requests

* fix: not given

* fix: setup

* feat: Added tenacity for retry

* fix: conftest

* test: Added tests

* fix: Rename

* fix: Modified test

* feat: stream support (unfinished)

* feat: Added tenacity for retry

* test: Added tests

* fix: Rename

* feat: stream support (unfinished)

* fix: single request creation

* feat: Support stream_cls

* fix: passed response_cls

* fix: Removed unnecessary json_to_response

* fix: imports

* fix: tests

* fix: imports

* fix: reponse parse

* fix: Added two examples to tests

* fix: sagemaker tests

* test: Added stream tests

* fix: comment out failing test

* fix: CR

* fix: Removed code

* docs: Added readme for streaming

* fix: condition

* docs: readme

* test: Added integration test for streaming

* fix: Added enter and close to stream

* fix: Uncomment chat completions test

* fix: poetry.lock

* fix: poetry.lock

* fix: Uncomment test case

* fix: Removed unused json_to_response ([`ae0d12b`](https://github.com/AI21Labs/ai21-python/commit/ae0d12b4e4fbb9cdf8e2fac20ec370e7f91215b4))

### Fix

* fix: delete file fixture (#116) ([`9d9a9ba`](https://github.com/AI21Labs/ai21-python/commit/9d9a9ba7a00a6efeb1fedb936633e5d35cec3527))

## v2.2.5 (2024-05-14)

### Chore

* chore(release): v2.2.5 [skip ci] ([`6d1502f`](https://github.com/AI21Labs/ai21-python/commit/6d1502f75457906f156503d9bbd63daf87665e54))

### Fix

* fix: upgrade ai21-tokenizer to latest version with less restrictive deps (#113)

* fix: upgrade ai21-tokenizer with latest version which has less restrictive deps

* fix: upgrade deps in general ([`022d60c`](https://github.com/AI21Labs/ai21-python/commit/022d60c78a1342fbe6a30a7a4d95c05b656a03bb))

## v2.2.4 (2024-05-09)

### Chore

* chore(release): v2.2.4 [skip ci] ([`aa2e8e2`](https://github.com/AI21Labs/ai21-python/commit/aa2e8e2fc4ca28728ed3f6b59abcbce398a04228))

### Fix

* fix: pass kwargs to endpoints (#110)

* feat: pass kwargs to endpoints

* fix: test when passing kwargs ([`0d895e4`](https://github.com/AI21Labs/ai21-python/commit/0d895e49330400e938d87ef5eaa75f8c34fe36d1))

## v2.2.3 (2024-04-25)

### Chore

* chore(release): v2.2.3 [skip ci] ([`58c0166`](https://github.com/AI21Labs/ai21-python/commit/58c01660400fe54c0034447e903a843bc92ffcd5))

### Fix

* fix: Support num_retries (#104)

* fix: num_retries method

* fix: Added 408 for retries ([`94c3254`](https://github.com/AI21Labs/ai21-python/commit/94c32542be3d4af6e80aae156b074055b9e5c34a))

## v2.2.2 (2024-04-24)

### Chore

* chore(release): v2.2.2 [skip ci] ([`f3daeba`](https://github.com/AI21Labs/ai21-python/commit/f3daebaeafd168090c7a9b06485c49ebfe4f1b87))

### Fix

* fix: Added raise error on wrong use of chat message (#102) ([`4efbea6`](https://github.com/AI21Labs/ai21-python/commit/4efbea6d85cd70f77650e4c4d96a3395eb60517b))

## v2.2.1 (2024-04-22)

### Chore

* chore(release): v2.2.1 [skip ci] ([`4fbfe00`](https://github.com/AI21Labs/ai21-python/commit/4fbfe0002bdf1e28bdfc611f1e9b9b99012f77c7))

* chore: update chat example (#95) ([`7dd83b1`](https://github.com/AI21Labs/ai21-python/commit/7dd83b184a21fe3d94a8a8b90f9bfe04c6e30e2e))

### Fix

* fix: Add support for n param to chat completion in studio (#98)

* fix: add n param support

* test: add integration test

* revert: wrong file

* fix: add n param support, add integration test ([`5459323`](https://github.com/AI21Labs/ai21-python/commit/54593235b590c35f5bfd391b3b195d294a65237b))

## v2.2.0 (2024-04-10)

### Chore

* chore(release): v2.2.0 [skip ci] ([`52a0fa3`](https://github.com/AI21Labs/ai21-python/commit/52a0fa3fe71f9491c89b12f183758eb9491a929d))

### Feature

* feat: Support new chat API (#93) ([`d14bb7c`](https://github.com/AI21Labs/ai21-python/commit/d14bb7c80c18cef8589515eeade1b917499ea09c))

## v2.1.3 (2024-03-27)

### Chore

* chore(release): v2.1.3 [skip ci] ([`a2b783c`](https://github.com/AI21Labs/ai21-python/commit/a2b783c6e1d7a095f69fc6cc3be86460e12949af))

* chore(deps-dev): bump black from 22.12.0 to 24.3.0 (#80)

* chore(deps-dev): bump black from 22.12.0 to 24.3.0

Bumps [black](https://github.com/psf/black) from 22.12.0 to 24.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.12.0...24.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;

* refactor: lint fixes

---------

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Gardin &lt;147075902+asafgardin@users.noreply.github.com&gt;
Co-authored-by: Asaf Gardin &lt;asafg@ai21.com&gt; ([`5986522`](https://github.com/AI21Labs/ai21-python/commit/59865220571bbdb19edf69aee16b21dbe7582d85))

* chore(deps): bump python-semantic-release/python-semantic-release (#85)

Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 9.3.0 to 9.3.1.
- [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.3.0...v9.3.1)

---
updated-dependencies:
- dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`aea5963`](https://github.com/AI21Labs/ai21-python/commit/aea5963943ad6220a41386acc5adbf23a8f0bf3e))

* chore(deps): bump python-semantic-release/python-semantic-release (#81)

Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 8.7.2 to 9.3.0.
- [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v8.7.2...v9.3.0)

---
updated-dependencies:
- dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Gardin &lt;147075902+asafgardin@users.noreply.github.com&gt; ([`c94966b`](https://github.com/AI21Labs/ai21-python/commit/c94966b4b05eec93a44e828800f043233b1fe5f4))

* chore(deps): bump pypa/gh-action-pypi-publish from 1.8.11 to 1.8.14 (#77)

Bumps [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) from 1.8.11 to 1.8.14.
- [Release notes](https://github.com/pypa/gh-action-pypi-publish/releases)
- [Commits](https://github.com/pypa/gh-action-pypi-publish/compare/2f6f737ca5f74c637829c0f5c3acd0e29ea5e8bf...81e9d935c883d0b210363ab89cf05f3894778450)

---
updated-dependencies:
- dependency-name: pypa/gh-action-pypi-publish
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Asaf Gardin &lt;147075902+asafgardin@users.noreply.github.com&gt; ([`7f3ea4a`](https://github.com/AI21Labs/ai21-python/commit/7f3ea4ab5ff87f92312e6fd873a17cbab010ed4e))

### Fix

* fix: Fix readme gaps (#87)

* docs: Added contextual answers examples and shared a link to our examples folder

* fix: Fixed main link in our readme

* docs: Examples section ([`da3afed`](https://github.com/AI21Labs/ai21-python/commit/da3afed67b806a35638ad804172183f8029619ea))

### Test

* test: integration test for library files (#83)

* fix: integration test for file

* refactor: Simplified

* fix: chat tests ([`3a50669`](https://github.com/AI21Labs/ai21-python/commit/3a50669db9351223ca971908eaa6e4842011d259))

* test: check imports (#76) ([`a72e23b`](https://github.com/AI21Labs/ai21-python/commit/a72e23b063ad3c1db076ced932bf0f4e6703c576))

## v2.1.2 (2024-02-27)

### Chore

* chore(release): v2.1.2 [skip ci] ([`9551776`](https://github.com/AI21Labs/ai21-python/commit/9551776a9f6c4c3a1671e308dad37a900e786b0f))

### Fix

* fix: Added future type annotation to sagemaker (#74) ([`f561dd8`](https://github.com/AI21Labs/ai21-python/commit/f561dd8ce2a2bd4e532f46fe96211486f9b8cc39))

## v2.1.1 (2024-02-25)

### Chore

* chore(release): v2.1.1 [skip ci] ([`69dc136`](https://github.com/AI21Labs/ai21-python/commit/69dc1361e47cdc60dde3c366dffe89b364fdce26))

### Fix

* fix: add logit bias to studio, sagemaker (#70)

* fix: add logit bias, fix studio completion

* fix: adjust tests

* fix: add logit bias integration test

* fix: update studio completion example

* fix: fix studio completion example

* fix: fix studio completion example

* fix: remove logit bias from bedrock

* fix: add logit bias to sagemaker completion, add params string

* fix: adjust tests

* fix: add logit bias integration test

* fix: update studio completion example

* fix: fix studio completion example

* fix: update code with new not_giving approach ([`b0b5bc1`](https://github.com/AI21Labs/ai21-python/commit/b0b5bc152d61944313b53f39cd314a621568e6e0))

## v2.1.0 (2024-02-25)

### Chore

* chore(release): v2.1.0 [skip ci] ([`5e9a768`](https://github.com/AI21Labs/ai21-python/commit/5e9a7681e4ab1ffcdcff1c07e0cb94452eb2632c))

### Feature

* feat: support NOT_GIVEN type (#69)

* feat: support NOT_GIVEN type

* fix: test when penalty is not passed

* fix: fix import, make more variants of penalty

* refactor: completion test refactor

* fix: rename endpoints

* fix: uncomment skip

---------

Co-authored-by: Asaf Gardin &lt;asafg@ai21.com&gt; ([`c7fd28a`](https://github.com/AI21Labs/ai21-python/commit/c7fd28a124c4971a9d9b85ad0d5fc5bd187535b0))

### Fix

* fix: Pass default model_id in bedrock client (#72)

* fix: Pass default model_id in bedrock client

* fix: Added validation for model_id

* fix: Added validation for model_id ([`e849d78`](https://github.com/AI21Labs/ai21-python/commit/e849d78dfa9990492dcd7836d2f5df3f1ade3451))

* fix: Pass model id in Bedrock client init (#71)

* feat: Moved model_id in bedrock to init

* test: Added tests to check model id

* fix: bedrock example

* refactor: rename test params ([`409e818`](https://github.com/AI21Labs/ai21-python/commit/409e818b751c261b93befedad968d6533860296c))

## v2.0.5 (2024-02-21)

### Chore

* chore(release): v2.0.5 [skip ci] ([`8965828`](https://github.com/AI21Labs/ai21-python/commit/896582839dd298121210187572adc178351f8d58))

### Fix

* fix: penalties in Sagemaker and Bedrock (#67)

* fix: penalties in sagemaker

* fix: don&#39;t pass None penalties to Bedrock

* fix: remove some default arge, and some unused args from bedrock model

* test: Added bedrock integration tests for penalties check

* ci: Integration tests on push

* fix: answer test

---------

Co-authored-by: etang &lt;etang@ai21.com&gt; ([`d7c912f`](https://github.com/AI21Labs/ai21-python/commit/d7c912f0ef86d8ca18a7225cdf8da6b79de8b415))

## v2.0.4 (2024-02-18)

### Chore

* chore(release): v2.0.4 [skip ci] ([`8b0f217`](https://github.com/AI21Labs/ai21-python/commit/8b0f217dd14aa820b5e404ed564e099d214d882f))

### Documentation

* docs: fix error handling example (#63) ([`fcd2746`](https://github.com/AI21Labs/ai21-python/commit/fcd2746ffd5839932628a10c0292fc766fef8963))

### Fix

* fix: Removed answer_length and mode from answer (#65)

* fix: Removed answer_length and mode from answer

* test: Fixed test ([`3814e57`](https://github.com/AI21Labs/ai21-python/commit/3814e57c7a90a026cfb4ee4f97b7edb0de937f16))

* fix: Add model types to docs (#62)

* fix: Added model names in readme

* fix: Added header ([`ca5c3ca`](https://github.com/AI21Labs/ai21-python/commit/ca5c3ca4127fa3393c1d29f069120b3896da8beb))

## v2.0.3 (2024-02-07)

### Chore

* chore(release): v2.0.3 [skip ci] ([`d0ccc5d`](https://github.com/AI21Labs/ai21-python/commit/d0ccc5d9f3a14a61fca788496afc65e02d9dca4f))

### Documentation

* docs: add code snippet notebook (#58)

* add code snippet notebook

* docs: add code snippet notebook

---------

Co-authored-by: Joshua Broyde &lt;joshuabroyde@Joshua-Broyde-PMGQ73FQ16.local&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt; ([`139d05f`](https://github.com/AI21Labs/ai21-python/commit/139d05f919d7c89da031dd50bf7bc1f080dc2d31))

### Fix

* fix: skip passing API key to ARN endpoint (#60) ([`8fd72f0`](https://github.com/AI21Labs/ai21-python/commit/8fd72f0ebe23bc23244e8453744b46bd093bccb3))

## v2.0.2 (2024-02-04)

### Chore

* chore(release): v2.0.2 [skip ci] ([`2db1816`](https://github.com/AI21Labs/ai21-python/commit/2db1816a152a20d18cbd397183512f479d4fec90))

* chore(deps): bump python-semantic-release/python-semantic-release (#49)

Bumps [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) from 8.3.0 to 8.7.2.
- [Release notes](https://github.com/python-semantic-release/python-semantic-release/releases)
- [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
- [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v8.3.0...v8.7.2)

---
updated-dependencies:
- dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: asafgardin &lt;147075902+asafgardin@users.noreply.github.com&gt; ([`aac9932`](https://github.com/AI21Labs/ai21-python/commit/aac993213edfe2ee889d5d12e899fe32e0ba702a))

### Fix

* fix: Changed log level (#56) ([`8db493c`](https://github.com/AI21Labs/ai21-python/commit/8db493c9ccd98e2421ff65a583e5e43773dc4bb1))

## v2.0.1 (2024-02-01)

### Chore

* chore(release): v2.0.1 [skip ci] ([`2af2f2b`](https://github.com/AI21Labs/ai21-python/commit/2af2f2b3153a486a8df33b4266f54cf28f0da049))

### Documentation

* docs: updated migration (#54)

* docs: updated migration

* fix: example ([`bca0424`](https://github.com/AI21Labs/ai21-python/commit/bca0424f44ffb2c5e5a3b9f292eb08649a844f53))

### Fix

* fix: Added badges (#55) ([`96d716d`](https://github.com/AI21Labs/ai21-python/commit/96d716de7a49868c20461bc2dc34c142da36070b))

## v2.0.0 (2024-01-31)

### Breaking

* feat: bump version (#53)

BREAKING CHANGE: 2.0.0 to SDK ([`77cfb85`](https://github.com/AI21Labs/ai21-python/commit/77cfb85d4b422ff217c511edfdf0782fce65c3b3))

### Chore

* chore(release): v2.0.0 [skip ci] ([`2a65f23`](https://github.com/AI21Labs/ai21-python/commit/2a65f23b487d7d64c09ea69f87daf1cd80a42146))

## v1.0.0 (2024-01-31)

### Chore

* chore(release): v1.0.0 [skip ci] ([`34efede`](https://github.com/AI21Labs/ai21-python/commit/34efedeb9a181bce86f8cbf0458dcd6b54538415))

* chore(release): v1.0.0 [skip ci] ([`66a0086`](https://github.com/AI21Labs/ai21-python/commit/66a008632304265914acb25a6eb8c6dfd8476911))

### Feature

* feat: bump to 2.0.0 (#52) ([`5e61e29`](https://github.com/AI21Labs/ai21-python/commit/5e61e29ec74c6c508969301c949e5b2bf72ad85b))

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

* Revert &#34;chore(release): v1.0.0 [skip ci]&#34; (#51)

This reverts commit 66a008632304265914acb25a6eb8c6dfd8476911. ([`6bab551`](https://github.com/AI21Labs/ai21-python/commit/6bab55101e3b17800c435442ae2a762ec39ce0f8))

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
