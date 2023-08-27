# Ввести два числа и определить какое из них больше
first = int(input('first digit '))
second = int(input('second digit '))


if first > second:
    print(f"first = {first} > second = {second}")

elif first == second:
     print(f"first = {first} = second = {second}")

else:  
    print(f"first = {first} < second = {second}")

