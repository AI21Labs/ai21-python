from ai21.clients.studio.ai21_client import AI21Client

client = AI21Client()
response = client.library.search.create(query="cat colors", max_segments=2)
print(response)
