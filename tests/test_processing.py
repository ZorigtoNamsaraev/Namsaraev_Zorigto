import pytest
from processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"state": "active", "date": "2023-01-01"},
        {"state": "inactive", "date": "2023-01-02"},
        {"state": "active", "date": "2023-01-03"},
    ]


def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, "active")
    assert len(result) == 2
    assert all(item["state"] == "active" for item in result)


def test_filter_by_state_no_matches(sample_data):
    result = filter_by_state(sample_data, "unknown")
    assert len(result) == 0


@pytest.mark.parametrize(
    "sort_order, expected_dates",
    [
        ("asc", ["2023-01-01", "2023-01-02", "2023-01-03"]),
        ("desc", ["2023-01-03", "2023-01-02", "2023-01-01"]),
    ],
)
def test_sort_by_date(sample_data, sort_order, expected_dates):
    sorted_data = sort_by_date(sample_data, sort_order)
    assert [item["date"] for item in sorted_data] == expected_dates
