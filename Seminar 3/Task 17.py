# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

lst = [1, 2, 3, 5, -1, 2, 6, 7, 2, 1, 5, 56, 3] 
print(lst)
lst1 = [] 
for i in lst: 
	if i not in lst1: 
		lst1.append(i) 
print(lst1)
print(len(lst1))

# print(len(set(lst))) - (множество) каждый элемент будет встречаться по одному, неупорядоченный тип данных. Длина уникальных элементов