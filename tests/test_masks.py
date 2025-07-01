import pytest

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number_edge_cases():
    edge_cases = [
        ("", True),
        ("1234-5678-1234-5678", "1234 **** **** 5678"),
        ("abcd", True),
        ("1234567890", True),
    ]

    for number, expected in edge_cases:
        if expected is True:
            with pytest.raises(ValueError):
                get_mask_card_number(number)
        else:
            assert get_mask_card_number(number) == expected


def test_get_mask_account_edge_cases():
    edge_cases = [
        ("", True),
        ("12345", "*2345"),
        ("xyz", True),
        ("123", True),
    ]

    for number, expected in edge_cases:
        if expected is True:
            with pytest.raises(ValueError):
                get_mask_account(number)
        else:
            assert get_mask_account(number) == expected


if __name__ == "__main__":
    pytest.main()
