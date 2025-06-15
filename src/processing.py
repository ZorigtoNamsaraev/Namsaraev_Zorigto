def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ Фильтрует список словарей по значению ключа 'state' """
    return [item for item in data if item.get('state') == state]


from datetime import datetime

def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """ Сортирует список словарей по полю 'date' """
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)