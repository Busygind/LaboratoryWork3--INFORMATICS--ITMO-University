#ISU % 4 = 3
import re

#СПОСОБ 1:
fin = open('test5.txt', encoding='UTF-8')
MY_GROUP = 'P3115'
for lines in fin:
    if re.fullmatch(r'[А-ЯЁ][а-яё]+ [А-ЯЁ]\.[А-ЯЁ]\. [A-Z]\d+\s', lines):
        surname, initials, group = lines.split()
        if initials[0] != initials[2] or group != MY_GROUP:
            print(surname, initials, group)

#СПОСОБ 2:
# fin = open('test2.txt', encoding='UTF-8')
# MY_GROUP = 'P3115'
# for lines in fin:
#     surname, initials, group = lines.split()
#     if initials[0] != initials[2] or group != MY_GROUP:
#         print(surname, initials, group)
