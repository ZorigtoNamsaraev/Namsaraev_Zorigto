def mask_card_number(number: str) -> str:
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def mask_account_number(number: str) -> str:
    return f"**{number[-8:]}"


def mask_account_card(data: str) -> str:
    """ Маскирует номер карты или счета, в зависимости от типа входной строки """
    if data.startswith("Счет"):
        parts = data.split()
        masked = mask_account_number(parts[-1])
        return f"{parts[0]} {masked}"
    else:
        *name_parts, number = data.split()
        masked = mask_card_number(number)
        return f"{' '.join(name_parts)} {masked}"


from datetime import datetime
def get_date(date_str: str) -> str:
    """ принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024") """
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается ISO формат.")