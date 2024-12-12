from ai21 import AI21Client
from pydantic import BaseModel

TIMEOUT = 20

CODE_STR = """def create_table_and_summary(user_message: str):\n    company_ticker = step(\n
instruction=f"hey, can you please extract company ticker from {user_message}? your answer should be a string that
contains only the ticker",\n        constraints=["a company ticker from a US exchange"],\n        output_type=str,\n
inputs=dict(),\n        allowed_tools=[],\n        ask_for_approval=True,\n    )\n
if not company_ticker or company_ticker == "I\'m sorry, I can\'t help with that.":\n
company_ticker = "AAPL"\n    table = step(\n        instruction=f"create table for company ticker {company_ticker}",\n
constraints=["should be a markdown table"],\n        output_type=str,\n        inputs=dict(),\n        allowed_tools=[],
\n    )\n\n    current_stock_price = api_step(\n
url=f"https://api.marketdata.app/v1/stocks/quotes/{company_ticker}/",  # noqa\n        method=HTTPMethod.GET,\n
headers=dict(\n            Accept="application/json",\n            User_Agent="PDL/1.0",\n
X_API_Version="1.0",\n        ),\n        credentials=[],\n    )\n    summary = step(\n
instruction=f"summarize table {table} in 3-5 bullet points",\n
constraints=["a company ticker from a US exchange"],\n        output_type=str,\n
inputs=dict(table=table, current_stock_price=current_stock_price),\n        allowed_tools=[],\n
ask_for_approval=True,\n    )\n    return summary"""


class ExampleSchema(BaseModel):
    name: str
    id: str


def main():
    ai21_client = AI21Client()

    assistant = ai21_client.beta.assistants.create(name="My Assistant")

    plan = ai21_client.beta.assistants.plans.create(
        assistant_id=assistant.id, code=CODE_STR, schemas=[ExampleSchema.model_json_schema()]
    )

    ai21_client.beta.assistants.routes.create(
        assistant_id=assistant.id, plan_id=plan.id, name="My Route", examples=["hi"], description="My Route Description"
    )


if __name__ == "__main__":
    main()
