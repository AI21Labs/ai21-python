from enum import Enum

from ai21 import AI21Client
from ai21.logger import set_verbose
from ai21.models.chat import ChatMessage
from ai21.models.chat.response_format import ResponseFormat
from pydantic import BaseModel

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
        role="system",
        content="As an assistant, your task is to generate structured data from user requests for zoo tickets. "
        "Create a valid JSON object specifying the date of the visit and the number of tickets. Your "
        "answer should be in JSON format, no extra spaces or new lines or any character that is not "
        f"part of the JSON. Here is the JSON format to follow: {ZooTicketsOrder.model_json_schema()}",
    ),
    ChatMessage(role="user", content="Can I order a ticket for September 22, 2024, for myself and two kids?"),
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-1.5",
    max_tokens=2000,
    temperature=0,
    response_format=ResponseFormat(type="text"),
)

print(response)

order = ZooTicketsOrder.model_validate_json(response.choices[0].message.content)

print(order)
