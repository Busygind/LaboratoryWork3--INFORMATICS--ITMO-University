#ISU % 4 = 3
import re

def ListOfMoneyReachers(filename):
    MY_GROUP = 'P3115'
    moneyReachers = []
    for lines in fin:
        if re.fullmatch(r'[А-ЯЁ][а-яё]+ [А-ЯЁ]\.[А-ЯЁ]\. [A-Z]\d+\s', lines):
            surname, initials, group = lines.split()
            if initials[0] != initials[2] or group != MY_GROUP:
                moneyReachers.append(surname + ' ' + initials + ' ' + group)
    return moneyReachers

for i in range(1,6):
    print('Ответ на тест ' + str(i))
    fin = open('test' + str(i) + '.txt', encoding='UTF-8')
    l = ListOfMoneyReachers(fin)
    for j in range(len(l)):
        print(l[j])
    print()

# Ответы на тесты:
# Ответ на тест 1
# Качок Я.Я. P0203
# Зумеров О.Г. P3115
# Ял О.Х. P3115
#
# Ответ на тест 2
# Петербургов П.Б. P3115
# Москвин М.Н. P3115
# Казанов К.Н. P8800
# Калининградов К.Н. P1337
# Тверин Т.Т. P3116
#
# Ответ на тест 3
# Симплов А.К. P3115
# Бумычев К.М. P3115
# Перфектов И.З. P3115
# Электроников Д.Ш. P3115
# Битов В.В. P3116
#
# Ответ на тест 4
# Бабабов Б.Б. P3116
# Гагабов Г.А. P3115
# Елебов Е.Ё. P3115
# Ёлебов Е.Е. P3116
# Зазабов З.А. P3115
#
# Ответ на тест 5
# Русский Д.А. P3115
# Правильный А.А. P3116

