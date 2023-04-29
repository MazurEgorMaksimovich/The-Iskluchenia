"""
Ошибки (номера строк через пробел, данная строка - №2): 28, 29, 32, 36!!!
"""


# В программе хранится словарь результатов ЗНО вида Предмет=Баллы.
# Узнать, проходит ли абитуриент на специальность, если нужно сдать
# все перечисленные экзамены с не меньшим количеством баллов.

neobkhodimye_ekzameny = {
    "Информатика": 180,
    "Математика": 185,
    "Украинский язык": 175
}

print("""Для определения возможности поступления, необходима информация о Вас.

Для ввода экзамена и баллов введите их через |: Химия | 40.
Для завершения ввода нажмите Enter.
""")

sdannye_ekzameny = {}

try:
    while True:
        vvod = input("").strip()
        if vvod == "":
            break

        ekzamen, ball = [x.strip() for x in vvod.split("|")]
        if int(ball) < 0:
            raise ValueError("Похоже, у Вас отрицательное количество баллов")
        elif int(ball) > 200:
            raise ValueError("Похоже, Ваше количество баллов больше максимального возможного")
        sdannye_ekzameny[ekzamen] = int(ball)

    print("Ваши экзамены:")
    if sdannye_ekzameny != {}:
        for i, (ekzamen, ball) in enumerate(sdannye_ekzameny.items(), start=1):
            print("{}) {} {}".format(i, ekzamen, ball))
    else:
        raise IndexError("Вы не сдали ни одного экзамена.")

    ok = False
    for neobkhodimyi_ekzamen, bally in neobkhodimye_ekzameny.items():
        if sdannye_ekzameny[neobkhodimyi_ekzamen] < bally:
            break
    else:
        ok = True

    print("Вы можете к нам поступить!" if ok else "Увы...")
except ValueError as err:
    print("Ошибочка вышла, " + str(err) + ". Проверьте введённые данные.")
except KeyError as err:
    print("Ошибочка вышла: Вы не сдали один или несколько необходимых экзаменов.")
except Exception as err:
    print("Ошибочка вышла: " + str(err))