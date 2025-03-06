import json

from enum import Enum

from pydantic import BaseModel

from ai21 import AI21Client
from ai21.logger import set_verbose
from ai21.models.chat import ChatMessage, ResponseFormat


set_verbose(True)


class TicketType(Enum):
    ADULT = "adult"
    CHILD = "child"


class ZooTicket(BaseModel):
    ticket_type: TicketType
    quantity: int


class ZooTicketsOrder(BaseModel):
    date: str
    tickets: list[ZooTicket]


messages = [
    ChatMessage(
        role="user",
        content="Please create a JSON object for ordering zoo tickets for September 22, 2024, "
        f"for myself and two kids, based on the following JSON schema: {ZooTicketsOrder.schema()}.",
    )
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-large-1.6-2025-03",
    max_tokens=800,
    temperature=0,
    response_format=ResponseFormat(type="json_object"),
)

zoo_order_json = json.loads(response.choices[0].message.content)
print(zoo_order_json)
