from ai21 import AI21Client

client = AI21Client()
response = client.embed.create(
    texts=["Holland is a geographical region[2] and former province on the western coast of the Netherlands."],
    type="segment",
)
print("embed: ", response.results[0].embedding)
