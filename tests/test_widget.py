import pytest
from widget import mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("4111111111111111", "4111 **** **** 1111"),
        ("1234567890123456", "************3456"),
        ("invalid_data", None),
    ],
)
def test_mask_account_card(input_data, expected_output):
    assert mask_account_card(input_data) == expected_output


@pytest.mark.parametrize(
    "invalid_input",
    [
        None,
        "",
        "not_a_card_or_account",
    ],
)
def test_mask_account_card_invalid_input(invalid_input):
    assert mask_account_card(invalid_input) is None
