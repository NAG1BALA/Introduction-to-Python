# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.

# sum(2, 2)
# # 4

x = int(input("Введите первое число = "))
n = int(input("Введите второе число = "))
tmp = None

if n > x:
    tmp = n
    n = x
    x = tmp

def sum(a,b):
 if b == 0:
  return a
 elif b > 0:
  return sum(a + 1, b - 1)
print(sum(x,n))


#РЕШЕНИЕ ОБРАЗЕЦ
# def sum(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     else:
#         return sum(a + 1, b - 1)