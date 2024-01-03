# CHANGELOG



## v2.0.0-rc.8 (2024-01-03)

### Fix

* fix: env vars to http client in sagemaker (#35)

* fix: env vars to http

* fix: env vars to http ([`4336c46`](https://github.com/AI21Labs/ai21-python/commit/4336c46352f61cae80f44e413059250a5fd9c409))

* fix: Pass env config to client ctor (#34)

* fix: removed application and organization

* fix: tests ([`4d4ef71`](https://github.com/AI21Labs/ai21-python/commit/4d4ef7161b156cfed21b010e57140af2c15dc1a4))

* fix: Added py.typed (#33) ([`6c9c0d0`](https://github.com/AI21Labs/ai21-python/commit/6c9c0d02d4df339efac1439a0ef5a0e4e2982587))

* fix: Added env config class to init (#32) ([`fa199c4`](https://github.com/AI21Labs/ai21-python/commit/fa199c4cfb00a2e28a054789801146a09d723fd0))


## v2.0.0-rc.7 (2024-01-02)

### Chore

* chore(release): v2.0.0-rc.7 [skip ci] ([`49a6ee1`](https://github.com/AI21Labs/ai21-python/commit/49a6ee1bd528b529315d101be0c0cd812839df70))

### Fix

* fix: Restructure packages (#31)

* refactor: moved classes to models package

* refactor: moved responses = to models package

* refactor: moved resources to common package

* refactor: chat message rename

* refactor: init

* fix: imports

* refactor: added more to imports ([`9e8a1f0`](https://github.com/AI21Labs/ai21-python/commit/9e8a1f05dc4afaecfc525fa22cb76594d6cf0c8d))


## v2.0.0-rc.6 (2024-01-02)

### Chore

* chore(release): v2.0.0-rc.6 [skip ci] ([`1ed334b`](https://github.com/AI21Labs/ai21-python/commit/1ed334b466acca6a8e03c49a387e5918b7a69d45))

### Fix

* fix: bump version ([`92c3f5d`](https://github.com/AI21Labs/ai21-python/commit/92c3f5de0b35510a3271a389160ab06cc064c7ea))

### Refactor

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

* fix: test ([`f84f86a`](https://github.com/AI21Labs/ai21-python/commit/f84f86ab4992701ba8ff22b262317e1b336ea785))


## v2.0.0-rc.5 (2023-12-27)

### Chore

* chore(release): v2.0.0-rc.5 [skip ci] ([`916c7b4`](https://github.com/AI21Labs/ai21-python/commit/916c7b40395eb2678cf4e66d49206fc94bbe9b73))

### Ci

* ci: Remove python 3_7 support (#25)

* ci: python 3.8 &gt;= support

* ci: unittests

* test: dummy test ([`d166253`](https://github.com/AI21Labs/ai21-python/commit/d166253a10456725107e80af9c13f9b360a47b0f))

### Documentation

* docs: Readme additions (#27)

* fix: removed unnecessary url env var

* fix: README.md CR ([`e4bb903`](https://github.com/AI21Labs/ai21-python/commit/e4bb903ef8775d9f755c6053e35176f407386342))

* docs: Readme migration (#24)

* docs: instance text

* docs: client instance explanation ([`53c53cb`](https://github.com/AI21Labs/ai21-python/commit/53c53cbd2f10556b54f41e313ec1cb4485657358))

* docs: README.md (#23)

* ci: updated precommit hooks

* docs: more readme updates

* docs: removed extra lines

* fix: rename

* docs: readme

* docs: full readme

* docs: badges

* ci: commitizen version

* revert: via ([`bbb87d3`](https://github.com/AI21Labs/ai21-python/commit/bbb87d351c6f71ead0616c8bb90b1715285861a6))

### Fix

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

* test: fixed ([`d6f73b5`](https://github.com/AI21Labs/ai21-python/commit/d6f73b5f3db3b234334b8e430d8a33633fb0247c))

### Test

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

* ci: removed unnecessary action ([`c455b77`](https://github.com/AI21Labs/ai21-python/commit/c455b77ce20555c530f02107f1400287e928b371))


## v2.0.0-rc.4 (2023-12-19)

### Chore

* chore(release): v2.0.0-rc.4 [skip ci] ([`2f53ec9`](https://github.com/AI21Labs/ai21-python/commit/2f53ec9abebd580a33c382cd1d544d234c74dbbf))

### Ci

* ci: Change main proj name (#22)

* ci: precommit

* fix: version name

* ci: Added rc pipeline for semantic release

* ci: pypi api keys

* ci: Added rc pipeline for semantic release

* ci: pypi api keys ([`2e87234`](https://github.com/AI21Labs/ai21-python/commit/2e87234e1d8b2c0a992c0a4e4d2b95727bd63209))

### Fix

* fix: readme ([`ef30164`](https://github.com/AI21Labs/ai21-python/commit/ef30164b09497ff8a7134e8868e1df9980104613))


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
