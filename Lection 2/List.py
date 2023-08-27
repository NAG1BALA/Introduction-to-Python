# list_1 = []
# list_1 = list()
# print(list_1)
# list_1 = [1, 2, 3, 8]
# print(*list_1) - вывести значение без скобок и запятых

# for i in list_1: - вывести значения построчно
#     print(i)

# print(list_1[-1]) - вывод значений с конца


# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) - функция добавления  в конец списка
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i) - добавляет значения от 0 до 5 поочередно
#     print(list_1)

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0 - pop удаляет и возвращает последний элемент
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12 - удаление по индексу конкретного элемента
# print(list_1) # [7, -1, 21, 0]

# list_1 = [12, 7, -1, 21, 0]
# print(list1.insert(2, 11)) - добавляет элемент на определенную позицию (число 11 на индекс 2)
# print(list1) # [12, 7, 11, -1, 21, 0]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]