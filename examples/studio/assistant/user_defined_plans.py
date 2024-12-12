from ai21 import AI21Client
from pydantic import BaseModel

TIMEOUT = 20


def test_func():
    pass


class ExampleSchema(BaseModel):
    name: str
    id: str


def main():
    ai21_client = AI21Client()

    assistant = ai21_client.beta.assistants.create(name="My Assistant")

    plan = ai21_client.beta.assistants.plans.create(assistant_id=assistant.id, code=test_func, schemas=[ExampleSchema])
    ai21_client.beta.assistants.routes.create(
        assistant_id=assistant.id, plan_id=plan.id, name="My Route", examples=["hi"], description="My Route Description"
    )


if __name__ == "__main__":
    main()
