# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120

number = int(input('Введите целое неотрицательное число - '))

i = 1
n = 1
while i <= number:
 n = i * n
 i = i + 1
else:
     print('Факториал равен')
print(n)