# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input('Введите число - '))

stepen = 1
i = 0
while stepen < number:
    i +=1
    print(stepen)
    stepen = 2**i
   
  