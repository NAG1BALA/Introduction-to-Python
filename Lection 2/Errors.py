SyntaxError('Синтаксическая ошибка')
number_first = 5
number_second = 7
if number_first > number_second # !!!!
    print(number_first)
# Отсутствие :


IndentationError('Ошибка отступов')
number_first = 5
number_second = 7
if number_first > number_second:
    print(number_first) # !!!!!
# Отсутствие отступов


TypeError('Типовая ошибка')
text = 'Python'
number = 5
print(text + number)
# Нельзя складывать строки и числа


ZeroDivisionError('Деление на 0')
number_first = 5
number_second = 0
print(number_first // number_second)
# Делить на 0 нельзя


KeyError('Ошибка ключа')
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])
# Такого ключа не существует



NameError('Ошибка имени переменной')
name = 'Ivan'
print(names)
# Переменной names не существует


ValueError('Ошибка значения')
text = 'Python'
print(int(text))
# Нельзя символы перевести в целые значения