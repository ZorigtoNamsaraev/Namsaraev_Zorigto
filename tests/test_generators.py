import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


# @pytest.fixture
# def transactions():
#     return [
#         {"id": 1, "operationAmount": {"amount": 100, "currency": {"code": "USD"}}},
#         {"id": 2, "operationAmount": {"amount": 200, "currency": {"code": "EUR"}}},
#         {"id": 3, "operationAmount": {"amount": 150, "currency": {"code": "USD"}}},
#     ]


def test_filter_by_currency(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    expected = [
        {"id": 1, "operationAmount": {"amount": 100, "currency": {"code": "USD"}}},
        {"id": 3, "operationAmount": {"amount": 150, "currency": {"code": "USD"}}},
    ]
    assert result == expected


def test_filter_by_currency_no_matches(transactions):
    result = list(filter_by_currency(transactions, "GBP"))
    assert result == []


def test_filter_by_currency_empty_list():
    assert list(filter_by_currency([], "USD")) == []


@pytest.mark.parametrize(
    "currency,expected",
    [
        (
            "USD",
            [
                {
                    "id": 1,
                    "operationAmount": {"amount": 100, "currency": {"code": "USD"}},
                },
                {
                    "id": 3,
                    "operationAmount": {"amount": 150, "currency": {"code": "USD"}},
                },
            ],
        ),
        (
            "EUR",
            [
                {
                    "id": 2,
                    "operationAmount": {"amount": 200, "currency": {"code": "EUR"}},
                }
            ],
        ),
        ("GBP", []),
    ],
)
def test_filter_by_currency_parametrized(transactions, currency, expected):
    result = list(filter_by_currency(transactions, currency))
    assert result == expected


def test_transaction_descriptions():
    transactions = [
        {
            "id": 1,
            "amount": 100,
            "currency": "USD",
            "type": "transfer",
            "from_account": "acc1",
            "to_account": "acc2",
        },
        {
            "id": 2,
            "amount": 200,
            "currency": "EUR",
            "type": "transfer",
            "from_card": "card1",
            "to_card": "card2",
        },
        {
            "id": 3,
            "amount": 150,
            "currency": "USD",
            "type": "transfer",
            "from_organization": "org1",
            "to_organization": "org2",
        },
        {"id": 4, "amount": 175, "currency": "JPY", "type": "unknown"},  # Unknown type
    ]

    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
        "Неизвестный тип транзакции",
    ]

    assert result == expected


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


def test_card_number_generator():
    expected_numbers = [f"{i:0>16}" for i in range(1000, 1005)]
    generated_numbers = list(card_number_generator(1000, 1004))
    assert generated_numbers == expected_numbers


def test_card_number_generator_empty():
    assert list(card_number_generator(0, -1)) == []


@pytest.mark.parametrize(
    "start,end,expected_counts",
    [
        (1000, 1005, 6),
        (2000, 2000, 1),
        (5000, 5005, 6),
    ],
)
def test_card_number_generator_parametrized(start, end, expected_counts):
    generated_numbers = list(card_number_generator(start, end))
    assert len(generated_numbers) == expected_counts
