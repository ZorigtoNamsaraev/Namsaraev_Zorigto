import pytest

@pytest.fixture
def sample_data():
    return [
        {"state": "active", "date": "2023-01-01"},
        {"state": "inactive", "date": "2023-01-02"},
        {"state": "active", "date": "2023-01-03"},
    ]

@pytest.fixture
def transactions():
    return [
        {"id": 1, "operationAmount": {"amount": 100, "currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"amount": 200, "currency": {"code": "EUR"}}},
        {"id": 3, "operationAmount": {"amount": 150, "currency": {"code": "USD"}}},
    ]
