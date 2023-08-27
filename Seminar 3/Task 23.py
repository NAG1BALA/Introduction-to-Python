# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

array = [0, -1, 5, 2, 3, 1, 0]
array1 = []
for i in range(len(array)):
    if array[i] > array[i-1]:
        array1.append(array[i])

print(len(array1))