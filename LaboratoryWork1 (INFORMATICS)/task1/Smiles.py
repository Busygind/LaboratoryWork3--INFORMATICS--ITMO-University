# ISU = 335103
# eyes = 3   nose = 3   mouth = 6
import re
def CountOfSmiles(filename):
    mySmile = re.compile(r'8<{P')
    return len(re.findall(mySmile, filename))

for i in range(1,6):
    fin = open('test' + str(i) + '.txt').read()
    print(CountOfSmiles(fin))

# Ответы, полученные без использования программы:
# 1: 49
# 2: 0
# 3: 5
# 4: 4
# 5: 8