import pytest
from ai21 import AI21Client


def test__when_model_and_model_id__raise_error():
    client = AI21Client()
    with pytest.raises(ValueError):
        client.completion.create(
            model="j2-ultra",
            model_id="j2-ultra",
            prompt="test prompt",
        )
