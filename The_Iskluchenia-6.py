"""
Ошибки (номера строк через пробел, данная строка - №2): 11 14 15
"""


def unemployment_rate(unemployed, employed):
    """Вернуть уровень безработицы (УБ) в долях 1.

       Расчет по формуле: УБ = Безработные / (Занятые + Безработные).
    """
    if unemployed + employed != 0:
        if unemployed >= 0 and employed >= 0:
            return unemployed / (unemployed + employed)
        else:
            raise ValueError("Людей не могёт быть отрицательное значеньице!!!")
    else:
            raise ZeroDivisionError("У Вас ноль людей.")


try:
    unemployed = int(input("Введите кол-во безработных (чел.): "))
    employed = int(input("Введите кол-во занятых (чел.): "))
    rate = unemployment_rate(unemployed, employed)
    print("Уровень безработицы = {:.1%}".format(rate))
except ValueError as err:
    print("Ошибочка вышла, " + str(err) + ". Проверьте введённые данные.")
except Exception as err:
    print("Ошибочка вышла: " + str(err))