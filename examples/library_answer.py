from ai21.clients.studio.ai21_client import AI21Client


client = AI21Client()
response = client.library.answer.create(question="Where is Thailand?")
print(response)
