from ai21 import AI21SageMakerClient

prompt = (
    "The following is a conversation between a user of an eCommerce store and a user operation"
    " associate called Max. Max is very kind and keen to help."
    " The following are important points about the business policies:\n- "
    "Delivery takes up to 5 days\n- There is no return option\n\nUser gender:"
    " Male.\n\nConversation:\nUser: Hi, had a question\nMax: "
    "Hi there, happy to help!\nUser: Is there no way to return a product?"
    " I got your blue T-Shirt size small but it doesn't fit.\n"
    "Max: I'm sorry to hear that. Unfortunately we don't have a return policy. \n"
    "User: That's a shame. \nMax: Is there anything else i can do for you?\n\n"
    "##\n\nThe following is a conversation between a user of an eCommerce store and a user operation"
    " associate called Max. Max is very kind and keen to help. The following are important points about"
    " the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\n"
    'User gender: Female.\n\nConversation:\nUser: Hi, I was wondering when you\'ll have the "Blue & White" '
    "t-shirt back in stock?\nMax: Hi, happy to assist! We currently don't have it in stock. Do you want me"
    " to send you an email once we do?\nUser: Yes!\nMax: Awesome. What's your email?\nUser: anc@gmail.com\n"
    "Max: Great. I'll send you an email as soon as we get it.\n\n##\n\nThe following is a conversation between"
    " a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help."
    " The following are important points about the business policies:\n- Delivery takes up to 5 days\n"
    "- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, how much time does it"
    " take for the product to reach me?\nMax: Hi, happy to assist! It usually takes 5 working"
    " days to reach you.\nUser: Got it! thanks. Is there a way to shorten that delivery time if i pay extra?\n"
    "Max: I'm sorry, no.\nUser: Got it. How do i know if the White Crisp t-shirt will fit my size?\n"
    "Max: The size charts are available on the website.\nUser: Can you tell me what will fit a young women.\n"
    "Max: Sure. Can you share her exact size?\n\n##\n\nThe following is a conversation between a user of an"
    " eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following"
    " are important points about the business policies:\n- Delivery takes up to 5 days\n"
    "- There is no return option\n\nUser gender: Female.\n\nConversation:\n"
    "User: Hi, I have a question for you"
)

client = AI21SageMakerClient(endpoint_name="sm_endpoint_name")
response = client.completion.create(prompt=prompt, max_tokens=2)

print(response)

print(response.prompt.tokens[0]["textRange"]["start"])
