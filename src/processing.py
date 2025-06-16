from typing import Dict
from typing import List
from typing import Optional


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция, которая сортирует список словарей по дате (ключ 'date')"""
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
