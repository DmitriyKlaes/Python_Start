# print('hello world')

# value = None
# print(type(a))
# print(type(b))
# value = 12334
# print(s)  # вывод строки


# s = "'hello world'"  # '"hello world"'
# a = 123
# b = 1.23
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)
# list = ['1','2','3','cool']
# col = ['sdf', 1,2,4.5,True]
# print(list)
# print(col)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, ' + ' , b, ' = ', a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# a = 1.312312654312
# b = 3
# c = round(a * b,5)
# print(c)

# a = 3
# a += 5
# print(a)

# a = 1 < 3 < 5 < 10
# print(a)
# func = 1
# T = 4
# x = 123
# print(func<T>(x))
# a = 1 > 2 or 4 < 6
# print(a)
# f = [1,2,3,4]
# print(f)
# print(not 2 in f)
# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Катя':
#     print('Ура, это же КАТЯ!')
# elif username == 'Марина':
#     print('Ничоси, это Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет, ', username)
    
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('stop')
#     print('it )')
# print(inverted)

# for i in 1,2,3,4,5:
#     print (i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)
    
# for i in range(1, 10, 2):
#     print(i)
    
# for i in 'qwe - rty':
#     print(i)

# text = 'съешь ещё этих мягких французских булок'

# # help(text.istitle)
# # help(int)
# # help(str)

# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue    
# for e in colors:
#     print(e*2) # redred greengreen blueblue    
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

def f(x):
    return x**2
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType