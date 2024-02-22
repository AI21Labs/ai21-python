from ai21.models import Penalty


def test_penalty__to_dict__when_has_not_given_fields__should_filter_them_out():
    penalty = Penalty(scale=0.5, apply_to_whitespaces=True)
    assert penalty.to_dict() == {"scale": 0.5, "applyToWhitespaces": True}
