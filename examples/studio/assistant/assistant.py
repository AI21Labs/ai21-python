from ai21 import AI21Client


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

    run = ai21_client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    if run.status == "completed":
        messages = ai21_client.beta.threads.messages.list(thread_id=thread.id)
        print("Messages:")
        print("\n".join(f"{msg.role}: {msg.content['text']}" for msg in messages.results))
    else:
        print(f"Run status: {run.status}")


if __name__ == "__main__":
    main()
