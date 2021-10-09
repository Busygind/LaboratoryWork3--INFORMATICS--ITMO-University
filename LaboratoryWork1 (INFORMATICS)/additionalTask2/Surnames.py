#ISU % 6 = 3
import re

fin = open('test5.txt', encoding='UTF-8')
surnames = []
rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
for string in fin:
    fios = re.findall(r'[А-ЯЁ][а-яё]* [А-ЯЁ]\.[А-ЯЁ]\.', string)
    for elem in fios:
        surnames.extend(elem.split()[::2])
surnames.sort(key=lambda x: rus_alphabet.index(x[0]))
for i in range(len(surnames)):
    print(surnames[i])

# Ответы на тесты, полученные без использования регулярных выражений:
# 1: Земцов
#    Леблон
#    Маттарнови
#    Трезини
#    Угрюмов
# 2: Баженов
#    Бецкой
#    Деламот
#    Растрелли
#    Старов
#    Фельтен
# 3: Белостоцкий
#    Гусарова
#    Карпенко
#    Мороз
#    Осадчего
# 4: Есенин
#    Лермонтов
#    Маяковский
#    Пушкин
# 5: Бэббидж
#    Буль
#    Бруевич
#    Брайль
#    Бодо
#    Дейкстра
#    Жаккард
#    Кнут
#    Морзе
#    Нейман
#    Тьюринг
#    Хемминг
#    Хаффман
#    Шеннон
#    Шелл
#    Эйкен
