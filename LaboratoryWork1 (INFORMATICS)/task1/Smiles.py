# ISU = 335103
# eyes = 3   nose = 3   mouth = 6

mySmile = '8<{P'
fin = open('test5.txt')
cnt = 0
for string in fin:
    cnt += string.count(mySmile)
print(cnt)

# Ответы, полученные без использования программы:
# 1: 49
# 2: 0
# 3: 5
# 4: 4
# 5: 8