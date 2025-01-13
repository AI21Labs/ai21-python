from ai21 import AI21Client
from pydantic import BaseModel

TIMEOUT = 20


def func():
    pass


class ExampleSchema(BaseModel):
    name: str
    id: str


def main():
    ai21_client = AI21Client()

    assistant = ai21_client.beta.assistants.create(name="My Assistant")

    plan = ai21_client.beta.assistants.plans.create(assistant_id=assistant.id, code=func, schemas=[ExampleSchema])
    ai21_client.beta.assistants.routes.create(
        assistant_id=assistant.id, plan_id=plan.id, name="My Route", examples=["hi"], description="My Route Description"
    )
    routes = ai21_client.beta.assistants.routes.list(assistant_id=assistant.id)
    print(f"Routes: {routes}")
    plans = ai21_client.beta.assistants.plans.list(assistant_id=assistant.id)
    print(f"Plans: {plans}")


if __name__ == "__main__":
    main()
