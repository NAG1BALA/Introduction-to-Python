# Напишите функцию f, которая на вход принимает два числа a и b, 
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 
a = 3
b = 5

def f(chislo, stepen):
  if stepen == 0:
    return 1
  elif stepen == 1:
    return chislo
  return chislo * f(chislo, stepen-1)
print(f(a,b))
  
 # РЕШЕНИЕ ОБРАЗЕЦ
# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a
# print(f(a,b))

 

