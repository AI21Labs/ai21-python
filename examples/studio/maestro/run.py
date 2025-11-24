from ai21 import AI21Client
from ai21.models.chat import ChatMessage
client = AI21Client(api_key="your_API_key")


def main():
    try:
        run_result = client.beta.maestro.runs.create_and_poll(
            input="Tell me about AI21 Maestro",
            requirements=[
                {
                    "name": "length requirement",
                    "description": "The length of the response should be less than 2000 characters",
                },
                {
                    "name": "source requirement",
                    "description": "Should rely on information from these websites: https://www.ai21.com/, https://www.ai21.com/maestro/, https://docs.ai21.com/home",
                },
            ],
            include=["requirements_result"],
        )

        print("\n=== AI21 MAESTRO INFO ===")
        print(run_result.result)
        print()
    except TimeoutError:
        print("The run timed out")


if __name__ == "__main__":
    main()
