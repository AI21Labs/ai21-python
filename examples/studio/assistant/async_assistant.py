import asyncio

from ai21 import AsyncAI21Client


async def main():
    ai21_client = AsyncAI21Client()

    assistant = await ai21_client.beta.assistants.create(name="My Assistant")

    thread = await ai21_client.beta.threads.create()

    await ai21_client.beta.threads.messages.create(thread_id=thread.id, role="user", content="Hello")

    run = await ai21_client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    if run.status == "completed":
        messages = await ai21_client.beta.threads.messages.list(thread_id=thread.id)
        print("Messages:")
        print("\n".join(f"{msg.role}: {msg.content['text']}" for msg in messages.results))
    elif run.status == "failed":
        raise Exception(f"Run failed. Status: {run.status}")
    else:
        print(f"Run status: {run.status}")


if __name__ == "__main__":
    asyncio.run(main())
