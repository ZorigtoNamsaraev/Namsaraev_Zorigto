def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Card number must be a 16-digit number")
    masked = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску."""
    account_number = account_number.strip()
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Account number must be numeric and at least 4 digits long")

    return f"**{account_number[-4:]}"
