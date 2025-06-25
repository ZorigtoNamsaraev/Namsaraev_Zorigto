# from datetime import datetime
from src.masks import get_mask_account
from src.masks import get_mask_card_number


def test_get_mask_card_number_edge_cases():
    edge_cases = [
        ("", ""),  # empty input
        ("1234-5678-1234-5678", "1234 **** **** 5678"),  # specific format
        ("abcd", "****"),  # non-numeric input
        ("1234567890", "****890"),  # different length
    ]

    for number, expected in edge_cases:
        assert get_mask_card_number(number) == expected


def test_get_mask_account_edge_cases():
    edge_cases = [
        ("", ""),  # empty input
        ("12345", "*****"),  # more digits than mask
        ("xyz", "***"),  # non-numeric input
    ]

    for number, expected in edge_cases:
        assert get_mask_account(number) == expected
