import pytest
from masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card_numbers():
    return [
        ("4111111111111111", "4111 **** **** 1111"),
        ("5500 0000 0000 0004", "5500 **** **** 0004"),
        ("3400-0000-0000-009", "3400 **** **** 0009"),
        ("", ""),
        ("123456", "123456"),
    ]


def test_get_mask_card_number(card_numbers):
    for number, expected in card_numbers:
        assert get_mask_card_number(number) == expected


@pytest.fixture
def account_numbers():
    return [
        ("1234567890123456", "************3456"),
        ("1234", ""),
        ("", ""),
        ("987654321", "*********321"),
    ]


def test_get_mask_account(account_numbers):
    for number, expected in account_numbers:
        assert get_mask_account(number) == expected
