from datetime import datetime


def mask_card_number(number: str) -> str:
    """Маскирует номер карты: первые 4, затем 2 видимые, далее звезды, и последние 4"""
    number = number.replace(" ", "")
    if len(number) != 16 or not number.isdigit():
        raise ValueError("Card number must be a 16-digit number")
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def mask_account_number(number: str) -> str:
    """Маскирует номер счёта: только последние 4 цифры"""
    number = number.replace(" ", "")
    if len(number) < 4 or not number.isdigit():
        raise ValueError("Account number must be numeric and at least 4 digits long")
    return f"**{number[-4:]}"


def mask_account_card(data: str) -> str:
    """Маскирует строку с номером карты или счёта"""
    data = data.strip()
    if data.startswith("Счет"):
        # Предполагается, что "Счет 73654108430135874305"
        parts = data.split()
        if len(parts) != 2:
            raise ValueError("Неверный формат строки для счета")
        _, number = parts
        masked = mask_account_number(number)
        return f"Счет {masked}"
    else:
        # Предполагается: "Visa Platinum 7000792289606361"
        *name_parts, number = data.split()
        name = " ".join(name_parts)
        masked = mask_card_number(number)
        return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """Преобразует дату ISO в формат ДД.ММ.ГГГГ"""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError(
            "Неверный формат даты. Ожидается ISO формат (например: '2024-03-11T02:26:18.671407')"
        )
