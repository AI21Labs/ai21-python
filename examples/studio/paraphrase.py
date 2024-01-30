from ai21 import AI21Client
from ai21.models import ParaphraseStyleType

client = AI21Client()
response = client.paraphrase.create(
    text="The cat (Felis catus) is a domestic species of small carnivorous mammal",
    style=ParaphraseStyleType.GENERAL,
    start_index=0,
    end_index=20,
)

print(response.suggestions[0].text)
print(response.suggestions[1].text)
print(response.suggestions[2].text)
