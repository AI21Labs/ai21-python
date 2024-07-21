from ai21.models import Penalty


def test_penalty__to_dict__when_has_not_given_fields__should_filter_them_out():
    penalty = Penalty(scale=0.5, apply_to_whitespaces=True)
    assert penalty.to_dict() == {"scale": 0.5, "applyToWhitespaces": True}


def test_penalty__to_json__when_has_not_given_fields__should_filter_them_out():
    penalty = Penalty(scale=0.5, apply_to_whitespaces=True)
    assert penalty.to_json() == '{"scale":0.5,"applyToWhitespaces":true}'


def test_penalty__from_dict__should_return_instance_with_given_values():
    penalty = Penalty.from_dict({"scale": 0.5, "applyToWhitespaces": True})
    assert penalty.scale == 0.5
    assert penalty.apply_to_whitespaces is True
    assert penalty.apply_to_emojis is None


def test_penalty__from_json__should_return_instance_with_given_values():
    penalty = Penalty.from_json('{"scale":0.5,"applyToWhitespaces":true}')
    assert penalty.scale == 0.5
    assert penalty.apply_to_whitespaces is True
    assert penalty.apply_to_emojis is None
