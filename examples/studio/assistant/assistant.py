import time

from ai21 import AI21Client

TIMEOUT = 20


def main():
    ai21_client = AI21Client()

    assistant = ai21_client.beta.assistants.create(name="My Assistant")

    thread = ai21_client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": "Hello",
            },
        ]
    )

    run = ai21_client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    start = time.time()

    while run.status == "in_progress":
        run = ai21_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        if time.time() - start > TIMEOUT:
            break
        time.sleep(1)

    if run.status == "completed":
        messages = ai21_client.beta.threads.messages.list(thread_id=thread.id)
        print("Messages:")
        print("\n".join(f"{msg.role}: {msg.content['text']}" for msg in messages.results))
    else:
        raise Exception(f"Run failed. Status: {run.status}")


if __name__ == "__main__":
    main()
