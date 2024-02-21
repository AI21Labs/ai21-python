from ai21 import AI21Client


client = AI21Client()
response = client.answer.create(
    context="Holland is a geographical region[2] and former province on the western coast of"
    " the Netherlands.[2] From the "
    "10th to the 16th century, Holland proper was a unified political region within the Holy Roman Empire as a county "
    "ruled by the counts of Holland. By the 17th century, the province of Holland had risen to become a maritime and "
    "economic power, dominating the other provinces of the newly independent Dutch Republic.",
    question="When did Holland become an economic power?",
)
print(response)
