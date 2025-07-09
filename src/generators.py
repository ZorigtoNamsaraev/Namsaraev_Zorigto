def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по заданному коду валюты"""
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        if transaction["type"] == "transfer":
            if transaction.get("from_account") and transaction.get("to_account"):
                yield "Перевод со счета на счет"
            elif transaction.get("from_card") and transaction.get("to_card"):
                yield "Перевод с карты на карту"
            elif transaction.get("from_organization") and transaction.get(
                "to_organization"
            ):
                yield "Перевод организации"
            else:
                yield "Неизвестный перевод"
        else:
            yield "Неизвестный тип транзакции"


def card_number_generator(start, end):
    for number in range(start, end + 1):
        formatted_number = f"{number:0>16}"
        yield formatted_number[:16]
