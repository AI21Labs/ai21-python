<h1 align="center">
    <a href="https://github.com/AI21Labs/ai21-python">AI21 Labs Python SDK</a>
</h1>

[//]: # "Add when public"
[//]: # '<a href="https://github.com/AI21Labs/ai21/actions?query=workflow%3ATest+event%3Apush+branch%3Amain"><img src="https://github.com/AI21Labs/ai21/actions/workflows/test.yaml/badge.svg" alt="Test"></a>'
[//]: # '<a href="https://pypi.org/project/ai21" target="_blank"><img src="https://img.shields.io/pypi/pyversions/ai21?color=%2334D058" alt="Supported Python versions"></a>'

<p align="center">
<a href="https://github.com/AI21Labs/ai21-python/actions/workflows/test.yaml"><img src="https://github.com/AI21Labs/ai21-python/actions/workflows/test.yaml/badge.svg?branch=main" alt="Test"></a>
<a href="https://github.com/AI21Labs/ai21-python/actions/workflows/integration-tests.yaml"><img src="https://github.com/AI21Labs/ai21-python/actions/workflows/integration-tests.yaml/badge.svg?branch=main" alt="Integration Tests"></a>
<a href="https://pypi.org/project/ai21" target="_blank"><img src="https://img.shields.io/pypi/v/ai21?color=%2334D058&label=pypi%20package" alt="Package version"></a>
<a href="https://python-poetry.org/" target="_blank"><img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" alt="Poetry"></a>
<a href="https://pypi.org/project/ai21" target="_blank"><img src="https://img.shields.io/pypi/pyversions/ai21?color=%2334D058" alt="Supported Python versions"></a>
<a href="https://github.com/semantic-release/semantic-release" target="_blank"><img src="https://img.shields.io/badge/semantic--release-python-e10079?logo=semantic-release" alt="Semantic Release Support"></a>
<a href="https://opensource.org/licenses/Apache-2.0" target="_blank"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
</p>

---

## Table of Contents

- [Examples](#examples-tldr) 🗂️
- [Migration from v1.3.4 and below](#migration-from-v134-and-below)
- [AI21 Official Documentation](#Documentation)
- [Installation](#Installation) 💿
- [Usage - Chat Completions](#Usage)
- [Conversational RAG (Beta)](#Conversational-RAG-Beta)
- [Older Models Support Usage](#Older-Models-Support-Usage)
- [More Models](#More-Models)
  - [Streaming](#Streaming)
  - [TSMs](#TSMs)
- [Token Counting](#Token-Counting)
- [Environment Variables](#Environment-Variables)
- [Error Handling](#Error-Handling)
- [Cloud Providers](#Cloud-Providers) ☁️
  - [AWS](#AWS)
    - [Bedrock](#Bedrock)
    - [SageMaker](#SageMaker)
  - [Azure](#Azure)
  - [Vertex](#Vertex)

## Examples (tl;dr)

If you want to quickly get a glance how to use the AI21 Python SDK and jump straight to business, you can check out the examples. Take a look at our models and see them in action! Several examples and demonstrations have been put together to show our models' functionality and capabilities.

### [Check out the Examples](examples/)

Feel free to dive in, experiment, and adapt these examples to suit your needs. We believe they'll help you get up and running quickly.

## Migration from v1.3.4 and below

In `v2.0.0` we introduced a new SDK that is not backwards compatible with the previous version.
This version allows for non-static instances of the client, defined parameters to each resource, modelized responses and
more.

<details>
<summary>Migration Examples</summary>

### Instance creation (not available in v1.3.4 and below)

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

- import ai21
- response = ai21.Completion.execute(model="j2-light", prompt=prompt, maxTokens=2)

+ from ai21 import AI21Client
+ client = ai21.AI21Client()
+ response = client.completion.create(model="j2-light", prompt=prompt, max_tokens=2)
```

This applies to all resources. You would now need to create a client instance and use it to call the resource method.

### Tokenization and Token counting before/after

```diff
- response = ai21.Tokenization.execute(text=prompt)
- print(len(response)) # number of tokens

+ from ai21 import AI21Client
+ client = AI21Client()
+ token_count = client.count_tokens(text=prompt)
```

### Key Access in Response Objects before/after

It is no longer possible to access the response object as a dictionary. Instead, you can access the response object as an object with attributes.

```diff
- import ai21
- response = ai21.Summarize.execute(source="some text", sourceType="TEXT")
- response["summary"]

+ from ai21 import AI21Client
+ from ai21.models import DocumentType
+ client = AI21Client()
+ response = client.summarize.create(source="some text", source_type=DocumentType.TEXT)
+ response.summary
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

## Documentation

---

The full documentation for the REST API can be found on [docs.ai21.com](https://docs.ai21.com/).

## Installation

---

```bash
pip install ai21
```

## Usage

---

```python
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

client = AI21Client(
    # defaults to os.enviorn.get('AI21_API_KEY')
    api_key='my_api_key',
)

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
]

chat_completions = client.chat.completions.create(
    messages=messages,
    model="jamba-1.5-mini",
)
```

### Async Usage

You can use the `AsyncAI21Client` to make asynchronous requests.
There is no difference between the sync and the async client in terms of usage.

```python
import asyncio

from ai21 import AsyncAI21Client
from ai21.models.chat import ChatMessage

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
]

client = AsyncAI21Client(
   # defaults to os.enviorn.get('AI21_API_KEY')
    api_key='my_api_key',
)


async def main():
    response = await client.chat.completions.create(
        messages=messages,
        model="jamba-1.5-mini",
    )

    print(response)


asyncio.run(main())

```

A more detailed example can be found [here](examples/studio/chat/chat_completions.py).

## Older Models Support Usage

<details>
<summary>Examples</summary>

### Supported Models:

- j2-light
- [j2-ultra](#Chat)
- [j2-mid](#Completion)
- [jamba-instruct](#Chat-Completion)

you can read more about the models [here](https://docs.ai21.com/reference/j2-complete-api-ref#jurassic-2-models).

### Chat

```python
from ai21 import AI21Client
from ai21.models import RoleType
from ai21.models import ChatMessage

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(text="Hello, I need help with a signup process.", role=RoleType.USER),
    ChatMessage(text="Hi Alice, I can help you with that. What seems to be the problem?", role=RoleType.ASSISTANT),
    ChatMessage(text="I am having trouble signing up for your product with my Google account.", role=RoleType.USER),
]


client = AI21Client()
chat_response = client.chat.create(
    system=system,
    messages=messages,
    model="j2-ultra",
)
```

For a more detailed example, see the chat [examples](examples/studio/chat.py).

### Completion

```python
from ai21 import AI21Client


client = AI21Client()
completion_response = client.completion.create(
    prompt="This is a test prompt",
    model="j2-mid",
)
```

### Chat Completion

```python
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
    ChatMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    ChatMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-instruct",
    max_tokens=100,
    temperature=0.7,
    top_p=1.0,
    stop=["\n"],
)

print(response)
```

Note that jamba-instruct supports async and streaming as well.

</details>

For a more detailed example, see the completion [examples](examples/studio/completion.py).

---

## Streaming

We currently support streaming for the Chat Completions API in Jamba.

```python
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

messages = [ChatMessage(content="What is the meaning of life?", role="user")]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-instruct",
    stream=True,
)
for chunk in response:
    print(chunk.choices[0].delta.content, end="")

```

### Async Streaming

```python
import asyncio

from ai21 import AsyncAI21Client
from ai21.models.chat import ChatMessage

messages = [ChatMessage(content="What is the meaning of life?", role="user")]

client = AsyncAI21Client()


async def main():
    response = await client.chat.completions.create(
        messages=messages,
        model="jamba-1.5-mini",
        stream=True,
    )
    async for chunk in response:
        print(chunk.choices[0].delta.content, end="")


asyncio.run(main())

```

---

### Conversational RAG (Beta)

Like chat, but with the ability to retrieve information from your Studio library.

```python
from ai21 import AI21Client
from ai21.models.chat import ChatMessage

messages = [
    ChatMessage(content="Ask a question about your files", role="user"),
]

client = AI21Client()

client.library.files.create(
  file_path="path/to/file",
  path="path/to/file/in/library",
  labels=["my_file_label"],
)
chat_response = client.beta.conversational_rag.create(
    messages=messages,
    labels=["my_file_label"],
)
```

For a more detailed example, see the chat [sync](examples/studio/conversational_rag/conversational_rag.py) and [async](examples/studio/conversational_rag/async_conversational_rag.py) examples.

---

## More Models

## TSMs

AI21 Studio's Task-Specific Models offer a range of powerful tools. These models have been specifically designed for their respective tasks and provide high-quality results while optimizing efficiency.
The full documentation and guides can be found [here](https://docs.ai21.com/docs/task-specific).

### Contextual Answers

The `answer` API allows you to access our high-quality question answering model.

```python
from ai21 import AI21Client

client = AI21Client()
response = client.answer.create(
    context="This is a text is for testing purposes",
    question="Question about context",
)
```

A detailed explanation on Contextual Answers, can be found [here](https://docs.ai21.com/docs/contextual-answers-api)

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

For more information on more Task Specific Models, see the [documentation](https://docs.ai21.com/reference/paraphrase-api-ref).

## Token Counting

---

By using the `count_tokens` method, you can estimate the billing for a given request.

```python
from ai21.tokenizers import get_tokenizer

tokenizer = get_tokenizer(name="jamba-tokenizer")
total_tokens = tokenizer.count_tokens(text="some text")  # returns int
print(total_tokens)
```

### Async Usage

```python
from ai21.tokenizers import get_async_tokenizer

## Your async function code
#...
tokenizer = await get_async_tokenizer(name="jamba-tokenizer")
total_tokens = await tokenizer.count_tokens(text="some text")  # returns int
print(total_tokens)
```

Available tokenizers are:

- `jamba-tokenizer`
- `j2-tokenizer`

For more information on AI21 Tokenizers, see the [documentation](https://github.com/AI21Labs/ai21-tokenizer).

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
from ai21.models import ChatMessage

client = AI21Client()

system = "You're a support engineer in a SaaS company"
messages = [
        # Notice the given role does not exist and will be the reason for the raised error
        ChatMessage(text="Hello, I need help with a signup process.", role="Non-Existent-Role"),
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

## Cloud Providers

---

### AWS

AI21 Library provides convenient ways to interact with two AWS clients for use with [AWS Bedrock](https://aws.amazon.com/bedrock/ai21/) and AWS SageMaker.

### Installation

---

```bash
pip install -U "ai21[AWS]"
```

This will make sure you have the required dependencies installed, including `boto3 >= 1.28.82`.

### Usage

---

### Bedrock

```python
from ai21 import AI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

client = AI21BedrockClient(region='us-east-1') # region is optional, as you can use the env variable instead

messages = [
  ChatMessage(content="You are a helpful assistant", role="system"),
  ChatMessage(content="What is the meaning of life?", role="user")
]

response = client.chat.completions.create(
    messages=messages,
    model_id=BedrockModelID.JAMBA_1_5_LARGE,
)
```

#### Stream

```python
from ai21 import AI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

system = "You're a support engineer in a SaaS company"
messages = [
    ChatMessage(content=system, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
    ChatMessage(content="Hi Alice, I can help you with that. What seems to be the problem?", role="assistant"),
    ChatMessage(content="I am having trouble signing up for your product with my Google account.", role="user"),
]

client = AI21BedrockClient()

response = client.chat.completions.create(
    messages=messages,
    model=BedrockModelID.JAMBA_1_5_LARGE,
    stream=True,
)

for chunk in response:
    print(chunk.choices[0].message.content, end="")
```

#### Async

```python
import asyncio
from ai21 import AsyncAI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

client = AsyncAI21BedrockClient(region='us-east-1') # region is optional, as you can use the env variable instead

messages = [
  ChatMessage(content="You are a helpful assistant", role="system"),
  ChatMessage(content="What is the meaning of life?", role="user")
]

async def main():
    response = await client.chat.completions.create(
        messages=messages,
        model_id=BedrockModelID.JAMBA_1_5_LARGE,
    )


asyncio.run(main())
```

### With Boto3 Session

```python
import boto3

from ai21 import AI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

boto_session = boto3.Session(region_name="us-east-1")

client = AI21BedrockClient(session=boto_session)

messages = [
  ChatMessage(content="You are a helpful assistant", role="system"),
  ChatMessage(content="What is the meaning of life?", role="user")
]

response = client.chat.completions.create(
    messages=messages,
    model_id=BedrockModelID.JAMBA_1_5_LARGE,
)
```

### Async

```python
import boto3
import asyncio

from ai21 import AsyncAI21BedrockClient, BedrockModelID
from ai21.models.chat import ChatMessage

boto_session = boto3.Session(region_name="us-east-1")

client = AsyncAI21BedrockClient(session=boto_session)

messages = [
  ChatMessage(content="You are a helpful assistant", role="system"),
  ChatMessage(content="What is the meaning of life?", role="user")
]

async def main():
  response = await client.chat.completions.create(
      messages=messages,
      model_id=BedrockModelID.JAMBA_1_5_LARGE,
  )

asyncio.run(main())
```

### SageMaker

```python
from ai21 import AI21SageMakerClient

client = AI21SageMakerClient(endpoint_name="j2-endpoint-name")
response = client.summarize.create(
    source="Text to summarize",
    source_type="TEXT",
)
print(response.summary)
```

#### Async

```python
import asyncio
from ai21 import AsyncAI21SageMakerClient

client = AsyncAI21SageMakerClient(endpoint_name="j2-endpoint-name")

async def main():
  response = await client.summarize.create(
      source="Text to summarize",
      source_type="TEXT",
  )
  print(response.summary)

asyncio.run(main())
```

### With Boto3 Session

```python
from ai21 import AI21SageMakerClient
import boto3
boto_session = boto3.Session(region_name="us-east-1")

client = AI21SageMakerClient(
    session=boto_session,
    endpoint_name="j2-endpoint-name",
)
```

### Azure

If you wish to interact with your Azure endpoint on Azure AI Studio, use the `AI21AzureClient`
and `AsyncAI21AzureClient` clients.

The following models are supported on Azure:

- `jamba-instruct`

```python
from ai21 import AI21AzureClient
from ai21.models.chat import ChatMessage

client = AI21AzureClient(
  base_url="https://<YOUR-ENDPOINT>.inference.ai.azure.com",
  api_key="<your Azure api key>",
)

messages = [
  ChatMessage(content="You are a helpful assistant", role="system"),
  ChatMessage(content="What is the meaning of life?", role="user")
]

response = client.chat.completions.create(
  model="jamba-1.5-mini",
  messages=messages,
)
```

#### Async

```python
import asyncio
from ai21 import AsyncAI21AzureClient
from ai21.models.chat import ChatMessage

client = AsyncAI21AzureClient(
  base_url="https://<YOUR-ENDPOINT>.inference.ai.azure.com/v1/chat/completions",
  api_key="<your Azure api key>",
)

messages = [
  ChatMessage(content="You are a helpful assistant", role="system"),
  ChatMessage(content="What is the meaning of life?", role="user")
]

async def main():
  response = await client.chat.completions.create(
    model="jamba-instruct",
    messages=messages,
  )

asyncio.run(main())
```

### Vertex

If you wish to interact with your Vertex AI endpoint on GCP, use the `AI21VertexClient`
and `AsyncAI21VertexClient` clients.

The following models are supported on Vertex:

- `jamba-1.5-mini`
- `jamba-1.5-large`

```python
from ai21 import AI21VertexClient

from ai21.models.chat import ChatMessage

# You can also set the project_id, region, access_token and Google credentials in the constructor
client = AI21VertexClient()

messages = ChatMessage(content="What is the meaning of life?", role="user")

response = client.chat.completions.create(
    model="jamba-1.5-mini",
    messages=[messages],
)
```

#### Async

```python
import asyncio

from ai21 import AsyncAI21VertexClient
from ai21.models.chat import ChatMessage

# You can also set the project_id, region, access_token and Google credentials in the constructor
client = AsyncAI21VertexClient()


async def main():
    messages = ChatMessage(content="What is the meaning of life?", role="user")

    response = await client.chat.completions.create(
        model="jamba-1.5-mini",
        messages=[messages],
    )

asyncio.run(main())
```

Happy prompting! 🚀
