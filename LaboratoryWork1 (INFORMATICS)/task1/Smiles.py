# ISU = 335103
# eyes = 3   nose = 3   mouth = 6
import re
def count_of_smiles(filename):
    my_smile = re.compile(r'8<{P')
    return len(re.findall(my_smile, filename))

for i in range(1,6):
    fin = open('test' + str(i) + '.txt').read()
    print(count_of_smiles(fin))

# Ответы, полученные без использования программы:
# 1: 49
# 2: 0
# 3: 5
# 4: 4
# 5: 8