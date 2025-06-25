import pytest

from widget import get_date
from widget import mask_account_number
from widget import mask_card_number

# from widget import mask_account_number
# from widget import mask_card_number


@pytest.mark.parametrize(
    "card_input, expected_output",
    [
        ("7000792289606361", "7000 ** **** 6361"),
        ("1234567812345678", "1234 ** **** 5678"),
    ],
)
def test_mask_card_number(card_input, expected_output):
    assert mask_card_number(card_input) == expected_output


@pytest.mark.parametrize(
    "account_input, expected_output",
    [
        ("73654108430135874305", "**3505"),
        ("123456789", "**6789"),
    ],
)
def test_mask_account_number(account_input, expected_output):
    assert mask_account_number(account_input) == expected_output


@pytest.mark.parametrize(
    "date_input, expected_output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2022-12-25T00:00:00", "25.12.2022"),
    ],
)
def test_get_date(date_input, expected_output):
    assert get_date(date_input) == expected_output


@pytest.mark.parametrize(
    "invalid_card_input",
    [
        "700079228960636",  # 15 digits
        "7000792289606362a",  # contains a letter
        "123456781234567",  # 15 digits
        "12345678123456789",  # 17 digits
        "",  # empty string
    ],
)
def test_invalid_card_number(invalid_card_input):
    with pytest.raises(ValueError):
        mask_card_number(invalid_card_input)
