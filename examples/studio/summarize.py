import os

os.environ["AI21_LOG_LEVEL"] = "debug"

from ai21.clients.studio.ai21_client import AI21Client

client = AI21Client()
response = client.summarize.create(
    source="Holland is a geographical region[2] and former province on the western coast of the Netherlands.[2] From the 10th to the 16th century, "
    "Holland proper was a unified political region within the Holy Roman Empire as a county ruled by the counts of Holland. By the 17th century, "
    "the province of Holland had risen to become a maritime and economic power, dominating the other provinces of the newly independent Dutch "
    "Republic.",
    source_type="TEXT",
)
print(response.summary)
