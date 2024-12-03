import asyncio

from ai21 import AsyncAI21Client


async def main():
    ai21_client = AsyncAI21Client()

    assistant = await ai21_client.beta.assistants.create(name="My Assistant")

    thread = await ai21_client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": {
                    "type": "text",
                    "text": "Hello",
                },
            },
        ]
    )

    run = await ai21_client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    while run.status == "in_progress":
        run = await ai21_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    if run.status == "completed":
        messages = await ai21_client.beta.threads.messages.list(thread_id=thread.id)
        print("Messages:")
        print("\n".join(f"{msg.role}: {msg.content['text']}" for msg in messages.results))


if __name__ == "__main__":
    asyncio.run(main())
