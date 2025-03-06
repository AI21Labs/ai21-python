import pytest

from ai21 import AI21BedrockClient, AsyncAI21BedrockClient, BedrockModelID
from ai21.models._pydantic_compatibility import _to_dict
from ai21.models.chat import ChatMessage


_SYSTEM_MSG = "You're a support engineer in a SaaS company"
_MESSAGES = [
    ChatMessage(content=_SYSTEM_MSG, role="system"),
    ChatMessage(content="Hello, I need help with a signup process.", role="user"),
]


def test_chat_completions__when_stream__last_chunk_should_hold_bedrock_metrics():
    client = AI21BedrockClient()
    response = client.chat.completions.create(
        messages=_MESSAGES,
        model=BedrockModelID.JAMBA_1_5_MINI,
        stream=True,
    )

    last_chunk = list(response)[-1]
    chunk_dict = _to_dict(last_chunk)
    assert "amazon-bedrock-invocationMetrics" in chunk_dict


@pytest.mark.asyncio
async def test__async_chat_completions__when_stream__last_chunk_should_hold_bedrock_metrics():
    client = AsyncAI21BedrockClient()
    response = await client.chat.completions.create(
        messages=_MESSAGES,
        model=BedrockModelID.JAMBA_1_5_MINI,
        stream=True,
    )

    last_chunk = [chunk async for chunk in response][-1]
    chunk_dict = _to_dict(last_chunk)
    assert "amazon-bedrock-invocationMetrics" in chunk_dict
