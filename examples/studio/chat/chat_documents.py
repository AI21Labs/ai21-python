import uuid

from ai21 import AI21Client
from ai21.logger import set_verbose
from ai21.models.chat import ChatMessage, DocumentSchema


set_verbose(True)

schnoodel = DocumentSchema(
    id=str(uuid.uuid4()),
    content="Schnoodel Inc. Annual Report - 2024. Schnoodel Inc., a leader in innovative culinary technology, saw a "
    "15% revenue growth this year, reaching $120 million. The launch of SchnoodelChef Pro has significantly "
    "contributed, making up 35% of total sales. We've expanded into the Asian market, notably Japan, "
    "and increased our global presence. Committed to sustainability, we reduced our carbon footprint "
    "by 20%. Looking ahead, we plan to integrate more advanced machine learning features and expand "
    "into South America.",
    metadata={"topic": "revenue"},
)
shnokel = DocumentSchema(
    id=str(uuid.uuid4()),
    content="Shnokel Corp. Annual Report - 2024. Shnokel Corp., a pioneer in renewable energy solutions, "
    "reported a 20% increase in revenue this year, reaching $200 million. The successful deployment of "
    "our advanced solar panels, SolarFlex, accounted for 40% of our sales. We entered new markets in Europe "
    "and have plans to develop wind energy projects next year. Our commitment to reducing environmental "
    "impact saw a 25% decrease in operational emissions. Upcoming initiatives include a significant "
    "investment in R&D for sustainable technologies.",
    metadata={"topic": "revenue"},
)

documents = [schnoodel, shnokel]

messages = [
    ChatMessage(
        role="system",
        content="You are a helpful assistant that receives revenue documents and answers related questions",
    ),
    ChatMessage(role="user", content="Hi, which company earned more during 2024 - Schnoodel or Shnokel?"),
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-1.5-mini-2025-02",
    documents=documents,
)

print(response)
