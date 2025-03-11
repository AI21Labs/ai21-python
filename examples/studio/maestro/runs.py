from ai21 import AI21Client

client = AI21Client()


def main():
    run_result = client.maestro.runs.create_and_poll(
        instruction="Who was the Maestro in the movie 'Maestro'?",
        tools=[{"type": "web_search"}],
        tool_resources={"web_search": {"urls": ["google.com"]}},
    )

    print(run_result)


if __name__ == "__main__":
    main()
