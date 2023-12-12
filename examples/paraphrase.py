from ai21.clients.studio.ai21_client import AI21Client


client = AI21Client()
response = client.paraphrase.create(text="The cat (Felis catus) is a domestic species of small carnivorous mammal")

print(response.suggestions[0].text)
print(response.suggestions[1].text)
print(response.suggestions[2].text)
