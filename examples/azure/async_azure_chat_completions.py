import asyncio

from ai21 import AsyncAI21AzureClient
from ai21.models.chat import ChatMessage


async def chat_completions():
    client = AsyncAI21AzureClient(
        base_url="<Your endpoint>",
        api_key="<your api key>",
    )

    messages = ChatMessage(content= 
                           "What is the meaning of life? Write a short poem inspired by Shakespeare. There should be 4 stanzas, each stanza has 6 lines. Iambic pentameter is used with a rhyme scheme of ABABCC and a reflective and descriptive tone.", 
                           role="user")

    completion = await client.chat.completions.create(
        model="jamba-instruct",
        messages=messages,
    )

    print(completion.to_json())


asyncio.run(chat_completions())
