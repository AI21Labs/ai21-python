from enum import Enum

from ai21 import AI21Client
from ai21.logger import set_verbose
from ai21.models.chat import ChatMessage
from ai21.models.chat.response_format import ResponseFormat
from pydantic import BaseModel, ValidationError

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
        content="Generate for a zoo tickets order json for for September 22, 2024, for myself and two kids using the"
        f"following JSON scheme: {ZooTicketsOrder.model_json_schema()}",
    )
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-1.5-large",
    max_tokens=2000,
    temperature=0,
    response_format=ResponseFormat(type="json_object"),
)

try:
    order = ZooTicketsOrder.model_validate_json(response.choices[0].message.content)
    print("Here is the order:")
    print(order.model_dump_json(indent=4))
except ValidationError as exc:
    print(exc)
