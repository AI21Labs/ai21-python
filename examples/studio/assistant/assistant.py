from ai21 import AI21Client


def main():
    ai21_client = AI21Client(
        api_key="413NQymWvgp83hNaqbA3EwYgqUjvREgn", api_host="https://api-stage.ai21.com/studio/v1"
    )

    assistant = ai21_client.beta.assistants.create(name="My Assistant")

    thread = ai21_client.beta.threads.create(
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

    run = ai21_client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )

    while run.status == "in_progress":
        run = ai21_client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    if run.status == "completed":
        messages = ai21_client.beta.threads.messages.list(thread_id=thread.id)
        print("Messages:")
        print("\n".join(f"{msg.role}: {msg.content['text']}" for msg in messages.results))
    else:
        # handle error or required action
        pass


if __name__ == "__main__":
    main()
