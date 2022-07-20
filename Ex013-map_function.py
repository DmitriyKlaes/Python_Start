li = [x for x in range(1, 20)]
print(li)

li = list(map(lambda x: x + 10, li))
print(li)


# data = list(map(str, input().split()))

# print(data)


# Возвращаемся к задаче 012 и используем мар

# def select(f, col):
#     return [f(x) for x in col] селект теперь не нужна.. мар выполняет ту же задачу
def where(f, col):
    return [x for x in col if f(x)]
data = '1 2 3 5 8 15 38'.split()
res = map(int, data)
res = where(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)