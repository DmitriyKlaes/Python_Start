# Множества

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21} # Неупорядоченная совокупность элементов
print(type(a))  # set
print(type(b))  # set

a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a))  # set
print(type(b))  # set
print(type(c))  # set
a = {1, 1, 1, 1, 1}
print(a)  # {1}

colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red')  # ok
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { }
print(colors)  # set()

a = {1, 2, 3, 5, 8}
b = frozenset(a) # Неизменяемое множество
print(b) # frozenset({1, 2, 3, 5, 8})