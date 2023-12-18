from ai21 import AI21Client


client = AI21Client()
response = client.library.answer.create(question="Where is Thailand?")
print(response)
