import os

os.environ["AI21_LOG_LEVEL"] = "debug"

from ai21.clients.studio.ai21_client import AI21Client

client = AI21Client()
response = client.improvements.create(
    text="Affiliated with the profession of project management, I have ameliorated myself with a different set of hard skills as well as soft skills.",
    types=["fluency"],
)

print(response.improvements[0].original_text)
print(response.improvements[0].suggestions)
print(response.improvements[0].suggestions[0])
print(response.improvements[0].improvement_type)
print(response.improvements[1].start_index)
print(response.improvements[1].end_index)
