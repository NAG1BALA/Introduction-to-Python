n = int(input())
res = 1
while n > 1:
    res *= n
    n -= 1
print(res)