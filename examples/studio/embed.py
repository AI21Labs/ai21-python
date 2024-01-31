from ai21 import AI21Client
from ai21.models import EmbedType

client = AI21Client()
response = client.embed.create(
    texts=["Holland is a geographical region[2] and former province on the western coast of the Netherlands."],
    type=EmbedType.SEGMENT,
)
print("embed: ", response.results[0].embedding)
