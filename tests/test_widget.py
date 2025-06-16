import pytest

from widget import mask_account_card


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 ** **** 6361"),
        ("Счет 73654108430135874305", "Счет **3505"),
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
        "Счет",
        "Visa 123456789012345",  # invalid card number (should be 16 digits)
        "Счет 123",  # invalid account number (less than 4 digits)
    ],
)
def test_mask_account_card_invalid_input(invalid_input):
    with pytest.raises(ValueError):
        mask_account_card(invalid_input)
