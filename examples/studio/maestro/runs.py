from ai21 import AI21Client

client = AI21Client()


def main():
    run_result = client.beta.maestro.runs.create_and_poll(
        input="Analyze the text below and determine who's the best pokemon ever",
        context={"text": "Psyduck is the best pokemon."},
    )

    print(run_result)


if __name__ == "__main__":
    main()
