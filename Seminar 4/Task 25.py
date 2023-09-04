# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

input_string = 'aaabcaadcdd'
midle = {}
output = []
for i in input_string:
    if i in midle:
        output.append(f'{i}_{midle[i]}')
    else:
        output.append(i)
    midle[i] = midle.get(i, 0)+1
result = (output)
print(result)

