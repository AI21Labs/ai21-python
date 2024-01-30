from ai21 import AI21Client

client = AI21Client()
response = client.library.search.create(query="cat colors", max_segments=2)
print(response)
