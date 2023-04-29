"""
Помилки (номери рядків через пробіл): !!!
"""


class NoMoneyToWithdrawError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PaymentError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Zashchita_ot_Obyegoroviniya(Exception):
    def __init__(self, message):
        super().__init__(message)


def print_accounts(accounts):
    """Печать аккаунтов."""
    print("Список клиентов ({}): ".format(len(accounts)))
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print("{}. {} {}".format(i, name, value))


def transfer_money(accounts, account_from, account_to, value):
    if value < 0:
        raise Zashchita_ot_Obyegoroviniya("Нельзя перевести отрицательную сумму деняк.")
    elif value > accounts[account_from]:
        raise NoMoneyToWithdrawError("Недостаточно средств для совершения транзакции.")
    else:
        account_from_money = accounts[account_from]
        account_to_money = accounts[account_to]
        try:
            accounts[account_from] -= value
            accounts[account_to] += value
        except Exception:
            accounts[account_from] = account_from_money
            accounts[account_to] = account_to_money
            raise PaymentError


if __name__ == "__main__":
    accounts = {
        "Вася Пупкин": 100,
        "Вася Табуреткин": 1500,
        "Вася Васильков": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Вася Пупкин",
        "account_to": "Вася Табуреткин"
    }

    print("Перевод от пользователя {account_from} пользователю {account_to}...".
          format(**payment_info))

    try:
        payment_info["value"] = int(input("Сумма = "))

        try:
            transfer_money(accounts, **payment_info)
        except Zashchita_ot_Obyegoroviniya as err:
            print()
            print(str(err))
            print()
        except NoMoneyToWithdrawError as err:
            print()
            print(str(err))
            print()
        except Exception:
            print()
            print("Произошла неизвестная ошибка.")
            print()
        else:
            print("OK!")
    except ValueError:
        print()
        print("Нерекомендуется пользоваться банковскими услугами в нетрезвом состоянии. Проверьте вводные данные.")
        print()

print_accounts(accounts)