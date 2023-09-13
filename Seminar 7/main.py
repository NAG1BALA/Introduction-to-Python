# def f(x):
#     return x


# print(f(6))
#                                         # ФУНКЦИЯ lambda
# f1 = lambda x: x
# print(f1(6))
# print((lambda x: x)(6))


x = "5 4 7 8 2 12"
print(x)
x1 = x.split()
print(x1)
x2 = list(map(lambda y: int(y)*3, x.split()))
print(x2)

x2 = list(filter(lambda y: y%8, x2))
print(x2)