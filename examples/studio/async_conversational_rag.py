import asyncio

from ai21 import AsyncAI21Client
from ai21.models import ChatMessage
from ai21.models._pydantic_compatibility import _to_dict

messages = [
    ChatMessage(text="Hello", role="user"),
    ChatMessage(text="Hi Alice, How can I help you today?", role="assistant"),
    ChatMessage(text="I'm looking for information about my deposits", role="user"),
    ChatMessage(text="Sure thing, ask away.", role="assistant"),
    ChatMessage(text="Can you explain why the length of deposit holds might change?", role="user"),
]


async def main():
    client = AsyncAI21Client()

    chat_response = await client.beta.conversational_rag.create(
        messages=messages,
        # you may add file IDs from your Studio library in order to question the model about their content
        # file_ids=["4455c74d-fd11-4161-a0bf-691e8f0f22cd'"]
    )

    print("Chat Response:", _to_dict(chat_response))


if __name__ == "__main__":
    asyncio.run(main())
