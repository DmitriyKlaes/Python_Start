# Словари

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left'])  # ←
# типы ключей могут отличаться


for k in dictionary.keys():
    print(k)

for k in dictionary.values():
    print(k)

for k in dictionary:
    print(dictionary[k])

print('next') # просто разделение

print(dictionary['up'])  # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left'])  # ⇐
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left']  # удаление элемента
for item in dictionary:  # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
