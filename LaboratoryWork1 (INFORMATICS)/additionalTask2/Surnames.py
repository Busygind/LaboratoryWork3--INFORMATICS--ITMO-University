#ISU % 6 = 3
import re

# fin = open('test5.txt', encoding='UTF-8')
def surnames_list_from_file(filename):
    surnames = []
    rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    for string in filename:
        fios = re.findall(r'[А-ЯЁ][а-яё]* [А-ЯЁ]\.[А-ЯЁ]\.', string)
        for elem in fios:
            surnames.extend(elem.split()[::2])
    surnames.sort(key=lambda x: rus_alphabet.index(x[0]))
    return surnames


for i in range(1,6):
    print('Ответ на тест ' + str(i))
    fin = open('test' + str(i) + '.txt', encoding='UTF-8')
    l = surnames_list_from_file(fin)
    for j in range(len(l)):
        print(l[j])
    print("\n")

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
