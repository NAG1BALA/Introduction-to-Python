# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# БЕЗ РЕКУРСИИ
# def check_num(x):
#     count = 0
#     for mult in range(2, x):
#         if x % mult == 0:
#             count += 1
#     if count == 0:
#         print("Число простое")
#     else:
#         print("Число не является простым")

# check_num(n)


# С РЕКУРСИЕЙ c ошибкой проверки если n = 2
# def recurs(x, count = 0, mult = 2):
#     if mult == x -1:
#            if count == 0:
#             print("Число простое")
#            else:
#             print("Число не является простым")
#            return
#     if x % mult == 0:
#      count += 1
#     return recurs(x, count, mult + 1)


# recurs(n)
n = 2

def is_prime(n, dil=2):
    if n <= 1:
        return False
    if n == 2 or dil * dil > n:
        print("Число простое")
        return True
    if n % dil == 0:
        return False
    return is_prime(n, dil + 1)

