import pytest
from src.widget import get_date, mask_account_number, mask_card_number, mask_account_card


@pytest.mark.parametrize(
    "account_card_input, expected_output",
    [
        ("Счет 123456789", "Счет **6789"),
        ("Имя Фамилия 7000792289606361", "Имя Фамилия 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(account_card_input, expected_output):
    assert mask_account_card(account_card_input) == expected_output

@pytest.mark.parametrize(
    "invalid_account_input",
    [
        "Счет 123",
        "Счет 123 abc",
        "Счет",
        "",
        "Некорректный ввод",
    ],
)
def test_invalid_account_card(invalid_account_input):
    with pytest.raises(ValueError):
        mask_account_card(invalid_account_input)

@pytest.mark.parametrize(
    "invalid_date_input",
    [
        "2024-03-32T02:26:18.671407",
        "some random text",
        "2022/12/25",
        "",
    ],
)
def test_invalid_date_format(invalid_date_input):
    with pytest.raises(ValueError):
        get_date(invalid_date_input)