<h1 align="center">
    <a href="https://github.com/AI21Labs/ai21">AI21 Labs Python SDK</a>
</h1>

<p align="center">
<a href="https://github.com/AI21Labs/ai21/actions?query=workflow%3ATest+event%3Apush+branch%3Amain"><img src="https://github.com/AI21Labs/ai21/actions/workflows/test.yaml/badge.svg" alt="Test"></a>
<a href="https://pypi.org/project/ai21" target="_blank"><img src="https://img.shields.io/pypi/v/ai21?color=%2334D058&label=pypi%20package" alt="Package version"></a>
<a href="https://pypi.org/project/ai21" target="_blank"><img src="https://img.shields.io/pypi/pyversions/ai21?color=%2334D058" alt="Supported Python versions"></a>
<a href="https://python-poetry.org/" target="_blank"><img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" alt="Poetry"></a>
<a href="https://github.com/semantic-release/semantic-release" target="_blank"><img src="https://img.shields.io/badge/semantic--release-python-e10079?logo=semantic-release" alt="Supported Python versions"></a>
<a href="https://opensource.org/licenses/Apache-2.0" target="_blank"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
</p>

---

## Installation

### pip

```bash
pip install ai21
```

AWS Client installation

```bash
pip install "ai21[AWS]"
```

## Migration from v1.3.3 and below

---

In `v2.0.0` we introduced a new SDK that is not backwards compatible with the previous version.
This version allows for Non static instances of the client, defined parameters to each resource, modelized responses and more.

### Instance creation (not available in v1.3.3 and below)

```python
from ai21 import AI21Client

client = AI21Client(api_key='my_api_key')

# or set api_key in environment variable - AI21_API_KEY and then
client = AI21Client()
```

### Completion before/after

```diff
prompt = "some prompt"

import ai21

- ai21.Completion.execute(model="j2-light", prompt=prompt, maxTokens=2)
+ client = ai21.AI21Client().completion(model="j2-light", prompt=prompt, max_tokens=2)

```
