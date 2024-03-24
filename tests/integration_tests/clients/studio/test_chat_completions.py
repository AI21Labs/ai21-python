from ai21 import AI21Client, AI21EnvConfig
from ai21.models import ChatMessage, RoleType
from ai21.models.responses.chat_completion_response import ChatCompletionResponse

AI21EnvConfig.api_host = "https://api-stage.ai21.com"

_MODEL = "gaia-small"
_MESSAGES = [
    ChatMessage(
        content="Hello, I need help studying for the coming test, can you teach me about the US constitution? ",
        role=RoleType.USER,
    ),
]


# TODO: When the api is officially released, update the test to assert the response
def test_chat_completion():
    num_results = 5
    messages = _MESSAGES

    client = AI21Client()
    response = client.chat.completions.create(
        model=_MODEL,
        messages=messages,
        num_results=num_results,
        max_tokens=64,
        logprobs=True,
        top_logprobs=0.6,
        temperature=0.7,
        stop=["\n"],
        top_p=0.3,
        frequency_penalty=0.2,
        presence_penalty=0.4,
    )

    assert isinstance(response, ChatCompletionResponse)
