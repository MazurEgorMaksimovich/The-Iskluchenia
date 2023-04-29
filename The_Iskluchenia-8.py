"""
Ошибки (номера строк через пробел, данная строка - №2): 9, 15, 18!!!
"""


# Дан список ФИО. Найти наиболее часто встречаемое отчество.
# Если отчества нет, человек не учитывается в подсчете.

try:
    n = int(input("Введите кол-во человек: "))

    middle_names = {}
    for i in range(n):
        fio = input("Введите ФИО через пробел: ").split()

        if len(fio) > 2:
            middle_name = fio[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1

    if len(middle_names) > 0:
        print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
        print("В расчете участвовало человек:", n)
    else:
        raise IndexError("На опрос никто не пришёл :(.")
except ValueError as err:
    print("Ошибочка вышла, " + str(err) + ". Проверьте введённые данные.")
except Exception as err:
    print("Ошибочка вышла: " + str(err))