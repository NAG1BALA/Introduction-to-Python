# Задачу необходимо решить через рекурсию
# Найти факториал числа N с помощью рекурсии

n = int(input("Введите новое число "))
def fact(x):
    if x == 1:
        return 1
    elif x < 1:
        print(f"Неправильный ввод данных")
        x = int(input("Введите новое число "))
        fact(x)
    return x * fact(x-1)
print(fact(n))