from enum import Enum

from pydantic import BaseModel, ValidationError

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
        f"for myself and two kids, based on the following JSON schema: {ZooTicketsOrder.model_json_schema()}.",
    )
]

client = AI21Client()

response = client.chat.completions.create(
    messages=messages,
    model="jamba-1.5-large",
    max_tokens=800,
    temperature=0,
    response_format=ResponseFormat(type="json_object"),
)

print(response)

try:
    order = ZooTicketsOrder.model_validate_json(response.choices[0].message.content)
    print("Zoo tickets order details JSON:")
    print(order.model_dump_json(indent=4))
except ValidationError as exc:
    print(exc)
