"""
Ошибки (номера строк через пробел, данная строка - №2): 11, 14, 15!!!
"""


def power(x, y=2):
    """Вернуть x^y."""
    if y == 0:
        return 1
    else:
        if y > 0:
            return x * power(x, y - 1)
        else:
            raise ValueError("Наша программа не умеет возводить в отрицательные степени, ибо рекурсия, попробуйте воспользоваться встроенным оператором '**'")


try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except ValueError as err:
    print("Ошибочка вышла, " + str(err) + ". Проверьте введённые данные.")
except Exception as err:
    print("Ошибочка вышла: " + str(err))