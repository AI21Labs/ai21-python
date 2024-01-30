<h1 align="center">
    <a href="https://github.com/AI21Labs/ai21">AI21 Labs Python SDK</a>
</h1>

[//]: # "Add when public"
[//]: # '<a href="https://github.com/AI21Labs/ai21/actions?query=workflow%3ATest+event%3Apush+branch%3Amain"><img src="https://github.com/AI21Labs/ai21/actions/workflows/test.yaml/badge.svg" alt="Test"></a>'
[//]: # '<a href="https://pypi.org/project/ai21" target="_blank"><img src="https://img.shields.io/pypi/pyversions/ai21?color=%2334D058" alt="Supported Python versions"></a>'

<p align="center">
<a href="https://pypi.org/project/ai21" target="_blank"><img src="https://img.shields.io/pypi/v/ai21?color=%2334D058&label=pypi%20package" alt="Package version"></a>
<a href="https://python-poetry.org/" target="_blank"><img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" alt="Poetry"></a>
<a href="https://github.com/semantic-release/semantic-release" target="_blank"><img src="https://img.shields.io/badge/semantic--release-python-e10079?logo=semantic-release" alt="Supported Python versions"></a>
<a href="https://opensource.org/licenses/Apache-2.0" target="_blank"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
</p>

---

## Migration from v1.3.3 and below

In `v2.0.0` we introduced a new SDK that is not backwards compatible with the previous version.
This version allows for Non static instances of the client, defined parameters to each resource, modelized responses and
more.

<details>
<summary>Migration Examples</summary>

### Instance creation (not available in v1.3.3 and below)

```python
from ai21 import AI21Client

client = AI21Client(api_key='my_api_key')

# or set api_key in environment variable - AI21_API_KEY and then
client = AI21Client()
```

We No longer support static methods for each resource, instead we have a client instance that has a method for each
allowing for more flexibility and better control.

### Completion before/after

```diff
prompt = "some prompt"

import ai21

- response = ai21.Completion.execute(model="j2-light", prompt=prompt, maxTokens=2)


+ client = ai21.AI21Client()
+ response = client.completion.create(model="j2-light", prompt=prompt, max_tokens=2)
```

This applies to all resources. You would now need to create a client instance and use it to call the resource method.

### Tokenization and Token counting before/after

```diff
- response = ai21.Tokenization.execute(text=prompt)
- print(len(response)) # number of tokens

+ client = ai21.AI21Client()
+ token_count = client.count_tokens(text=prompt)
```

---

### AWS Client Creations

### Bedrock Client creation before/after

```diff
- import ai21
- destination = ai21.BedrockDestination(model_id=ai21.BedrockModelID.J2_MID_V1)
- response = ai21.Completion.execute(prompt=prompt, maxTokens=1000, destination=destination)

+ from ai21 import AI21BedrockClient, BedrockModelID
+ client = AI21BedrockClient()
+ response = client.completion.create(prompt=prompt, max_tokens=1000, model_id=BedrockModelID.J2_MID_V1)
```

### SageMaker Client creation before/after

```diff
- import ai21
- destination = ai21.SageMakerDestination("j2-mid-test-endpoint")
- response = ai21.Completion.execute(prompt=prompt, maxTokens=1000, destination=destination)

+ from ai21 import AI21SageMakerClient
+ client = AI21SageMakerClient(endpoint_name="j2-mid-test-endpoint")
+ response = client.completion.create(prompt=prompt, max_tokens=1000)
```

</details>

## Installation

### pip

```bash
pip install ai21
```

## Usage

---

### Client Instance Creation

```python
from ai21 import AI21Client

client = AI21Client(
    # defaults to os.enviorn.get('AI21_API_KEY')
    api_key='my_api_key',
)

response = client.completion.create(
    prompt="<your prompt here>",
    max_tokens=10,
    model="j2-mid",
    temperature=0.3,
    top_p=1,
)

print(response.completions)
print(response.prompt)
```

### Token Counting

---

By using the `count_tokens` method, you can estimate the billing for a given request.

```python
from ai21 import AI21Client

client = AI21Client()
client.count_tokens(text="some text")  # returns int
```

### File Upload

---

```python
from ai21 import AI21Client

client = AI21Client()

file_id = client.library.files.create(
    file_path="path/to/file",
    path="path/to/file/in/library",
    labels=["label1", "label2"],
    public_url="www.example.com",
)

uploaded_file = client.library.files.get(file_id)
```

## Environment Variables

---

You can set several environment variables to configure the client.

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

To enable logging, set the `AI21_LOG_LEVEL` environment variable.

```bash
$ export AI21_LOG_LEVEL=debug
```

### Other Important Environment Variables

- `AI21_API_KEY` - Your API key. If not set, you must pass it to the client constructor.
- `AI21_API_VERSION` - The API version. Defaults to `v1`.
- `AI21_API_HOST` - The API host. Defaults to `https://api.ai21.com/v1/`.
- `AI21_TIMEOUT_SEC` - The timeout for API requests.
- `AI21_NUM_RETRIES` - The maximum number of retries for API requests. Defaults to `3` retries.
- `AI21_AWS_REGION` - The AWS region to use for AWS clients. Defaults to `us-east-1`.

## Error Handling

---

```python
from ai21 import errors as ai21_errors
from ai21 import AI21Client, AI21APIError

client = AI21Client()

system = "You're a support engineer in a SaaS company"
messages = [
    {
        "text": "Hello, I need help with a signup process.",
        "role": "user",
        "name": "Alice",
    },
]

try:
    chat_completion = client.chat.create(
        messages=messages,
        model="j2-ultra",
        system=system
    )
except ai21_errors.AI21ServerError as e:
    print("Server error and could not be reached")
    print(e.details)
except ai21_errors.TooManyRequestsError as e:
    print("A 429 status code was returned. Slow down on the requests")
except AI21APIError as e:
    print("A non 200 status code error. For more error types see ai21.errors")

```

## AWS Clients

---

AI21 Library provides convenient ways to interact with two AWS clients for use with AWS SageMaker and AWS Bedrock.

### Installation

---

```bash
pip install "ai21[AWS]"
```

This will make sure you have the required dependencies installed, including `boto3 >= 1.28.82`.

### Usage

---

#### SageMaker

```python
from ai21 import AI21SageMakerClient

client = AI21SageMakerClient(endpoint_name="j2-endpoint-name")
response = client.summarize.create(
    source="Text to summarize",
    source_type="TEXT",
)
print(response.summary)
```

#### With Boto3 Session

```python
from ai21 import AI21SageMakerClient
import boto3
boto_session = boto3.Session(region_name="us-east-1")

client = AI21SageMakerClient(
    session=boto_session,
    endpoint_name="j2-endpoint-name",
)
```

#### Bedrock

---

```python
from ai21 import AI21BedrockClient, BedrockModelID

client = AI21BedrockClient(region='us-east-1') # region is optional, as you can use the env variable instead
response = client.completion.create(
    prompt="Your prompt here",
    model_id=BedrockModelID.J2_MID_V1,
    max_tokens=10,
)
print(response.completions[0].data.text)
```

#### With Boto3 Session

```python
from ai21 import AI21BedrockClient, BedrockModelID
import boto3
boto_session = boto3.Session(region_name="us-east-1")

client = AI21BedrockClient(
    session=boto_session,
)

response = client.completion.create(
    prompt="Your prompt here",
    model_id=BedrockModelID.J2_MID_V1,
    max_tokens=10,
)
```
