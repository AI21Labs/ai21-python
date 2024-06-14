from ai21 import AI21AzureClient

from ai21.models.chat import ChatMessage

client = AI21AzureClient(
    base_url="<Your endpoint>",
    api_key="<your api key>",
)

messages = ChatMessage(content=
                       "What is the meaning of life? Write a short poem inspired by Shakespeare. There should be 4 stanzas, each stanza has 6 lines. Iambic pentameter is used with a rhyme scheme of ABABCC and a reflective and descriptive tone.", 
                       role="user")

completion = client.chat.completions.create(
    model="jamba-instruct",
    messages= messages,
    temperature = 1.0, # Setting =1 allows for greater variability per API call.
    top_p = 1.0 # Setting =1 allows full sample of tokens to be considered per API call.
)

print(completion.to_json())
