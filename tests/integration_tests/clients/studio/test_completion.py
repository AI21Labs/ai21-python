import pytest

from ai21 import AI21Client
from ai21.models import Penalty

_PROMPT = (
    "The following is a conversation between a user of an eCommerce store and a user operation"
    " associate called Max. Max is very kind and keen to help."
    " The following are important points about the business policies:\n- "
    "Delivery takes up to 5 days\n- There is no return option\n\nUser gender:"
    " Male.\n\nConversation:\nUser: Hi, had a question\nMax: "
    "Hi there, happy to help!\nUser: Is there no way to return a product?"
    " I got your blue T-Shirt size small but it doesn't fit.\n"
    "Max: I'm sorry to hear that. Unfortunately we don't have a return policy. \n"
    "User: That's a shame. \nMax: Is there anything else i can do for you?\n\n"
    "##\n\nThe following is a conversation between a user of an eCommerce store and a user operation"
    " associate called Max. Max is very kind and keen to help. The following are important points about"
    " the business policies:\n- Delivery takes up to 5 days\n- There is no return option\n\n"
    'User gender: Female.\n\nConversation:\nUser: Hi, I was wondering when you\'ll have the "Blue & White" '
    "t-shirt back in stock?\nMax: Hi, happy to assist! We currently don't have it in stock. Do you want me"
    " to send you an email once we do?\nUser: Yes!\nMax: Awesome. What's your email?\nUser: anc@gmail.com\n"
    "Max: Great. I'll send you an email as soon as we get it.\n\n##\n\nThe following is a conversation between"
    " a user of an eCommerce store and a user operation associate called Max. Max is very kind and keen to help."
    " The following are important points about the business policies:\n- Delivery takes up to 5 days\n"
    "- There is no return option\n\nUser gender: Female.\n\nConversation:\nUser: Hi, how much time does it"
    " take for the product to reach me?\nMax: Hi, happy to assist! It usually takes 5 working"
    " days to reach you.\nUser: Got it! thanks. Is there a way to shorten that delivery time if i pay extra?\n"
    "Max: I'm sorry, no.\nUser: Got it. How do i know if the White Crisp t-shirt will fit my size?\n"
    "Max: The size charts are available on the website.\nUser: Can you tell me what will fit a young women.\n"
    "Max: Sure. Can you share her exact size?\n\n##\n\nThe following is a conversation between a user of an"
    " eCommerce store and a user operation associate called Max. Max is very kind and keen to help. The following"
    " are important points about the business policies:\n- Delivery takes up to 5 days\n"
    "- There is no return option\n\nUser gender: Female.\n\nConversation:\n"
    "User: Hi, I have a question for you"
)


def test_completion():
    num_results = 3

    client = AI21Client()
    response = client.completion.create(
        prompt=_PROMPT,
        max_tokens=64,
        model="j2-ultra",
        temperature=1,
        top_p=0.2,
        top_k_return=0,
        stop_sequences=["##"],
        num_results=num_results,
        custom_model=None,
        epoch=1,
        count_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        frequency_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
        presence_penalty=Penalty(
            scale=0,
            apply_to_emojis=False,
            apply_to_numbers=False,
            apply_to_stopwords=False,
            apply_to_punctuation=False,
            apply_to_whitespaces=False,
        ),
    )

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == num_results
    # Check the results aren't all the same
    assert len(set([completion.data.text for completion in response.completions])) == num_results
    for completion in response.completions:
        assert isinstance(completion.data.text, str)


def test_completion_when_temperature_1_and_top_p_is_0__should_return_same_response():
    num_results = 5

    client = AI21Client()
    response = client.completion.create(
        prompt=_PROMPT,
        max_tokens=64,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        top_k_return=0,
        num_results=num_results,
        epoch=1,
    )

    assert response.prompt.text == _PROMPT
    assert len(response.completions) == num_results
    # Verify all results are the same
    assert len(set([completion.data.text for completion in response.completions])) == 1


@pytest.mark.parametrize(
    ids=[
        "finish_reason_length",
        "finish_reason_endoftext",
        "finish_reason_stop_sequence",
    ],
    argnames=["max_tokens", "stop_sequences", "reason"],
    argvalues=[
        (10, "##", "length"),
        (100, "##", "endoftext"),
        (50, "\n", "stop"),
    ],
)
def test_completion_when_finish_reason_defined__should_halt_on_expected_reason(
    max_tokens: int, stop_sequences: str, reason: str
):
    client = AI21Client()
    response = client.completion.create(
        prompt=_PROMPT,
        max_tokens=max_tokens,
        model="j2-ultra",
        temperature=1,
        top_p=0,
        num_results=1,
        stop_sequences=[stop_sequences],
        top_k_return=0,
        epoch=1,
    )

    assert response.completions[0].finish_reason.reason == reason
