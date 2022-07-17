# Кортежи (неизменяемый список)

a = (3, 1, 41, 4)
print(a)
print(a[-2])

t = ()
print(type(t))  # tuple
t = (1,)
print(type(t))  # tuple
t = (1)
print(type(t))  # int
t = (28, 9, 1990)
print(type(t))  # tuple
colors = ['red', 'green', 'blue']
print(colors)  # ['red', 'green', 'blue']
t = tuple(colors)
print(t)  # ('red', 'green', 'blue')


t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2])  # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
    print(e)  # red green blue
# t[0] = 'black'  # TypeError: 'tuple' object does not support item assignment


t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue
