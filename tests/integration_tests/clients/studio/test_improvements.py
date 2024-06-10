import pytest

from ai21 import AI21Client, AsyncAI21Client
from ai21.models import ImprovementType


def test_improvements():
    client = AI21Client()
    response = client.improvements.create(
        text="Affiliated with the profession of project management,"
        " I have ameliorated myself with a different set of hard skills as well as soft skills.",
        types=[ImprovementType.FLUENCY],
    )

    assert len(response.improvements) > 0


@pytest.mark.asyncio
async def test_async_improvements():
    client = AsyncAI21Client()
    response = await client.improvements.create(
        text="Affiliated with the profession of project management,"
        " I have ameliorated myself with a different set of hard skills as well as soft skills.",
        types=[ImprovementType.FLUENCY],
    )

    assert len(response.improvements) > 0
