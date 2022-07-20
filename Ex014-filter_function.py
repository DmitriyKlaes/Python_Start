data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))
print(res)


# Возвращаемся к задаче 012 и 013 и используем фмльтр

# def select(f, col):
#     return [f(x) for x in col] селект теперь не нужна.. мар выполняет ту же задачу
# def where(f, col):
#     return [x for x in col if f(x)] вэа теперь нам тоже не нужна, делаем фильтр
data = '1 2 3 5 8 15 38'.split()
res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x**2), res))
print(res)