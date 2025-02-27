# A

print(''.join(set(input())))

# B

s1 = set(input())
s2 = set(input())

print(''.join(s1 & s2))

# C

word_list = []
for _ in range(int(input())):
    word_list.extend(input().split(' '))
print('\n'.join(set(word_list)))

# D

n, m = int(input()), int(input())
s1, s2 = set(), set()

for _ in range(n):
    s1.add(input())

for _ in range(m):
    s2.add(input())

s_len = len(s1 & s2)

print('Таких нет' if s_len == 0 else s_len)

# E

a, b = int(input()), int(input())
porridges = []
for _ in range(a + b):
    porridges.append(input())
both = len([i for i in porridges if porridges.count(i) == 1])
print(both if both else 'Таких нет')

# F

a, b = int(input()), int(input())
porridges = []

for _ in range(a + b):
    if (x := input()) not in porridges:
        porridges.append(x)
    else:
        porridges.remove(x)
if len(porridges):
    for kid in sorted(porridges):
        print(kid)
else:
    print('Таких нет')

# G

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' ',
}
line = input()
for letter in line:
    print(MORSE[letter.upper()], end=' ' if letter != ' ' else '\n')

# H

kids = []

for _ in range(int(input())):
    kids.extend([input().split()])

kids.sort()

key, counter = input(), 0

for kid in kids:
    if key in kid[1:]:
        print(kid[0])
        counter += 1
if not counter:
    print('Таких нет')
    
# I

count_dict = {}

while (s := input()) != '':
    words_list = s.split()
    for word in words_list:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
            
for key, value in count_dict.items():
    print(f"{key} {value}")

# J

LITER = {
    'А': 'A', 'Б': 'B', 'В': 'V',
    'Г': 'G', 'Д': 'D', 'Е': 'E',
    'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K',
    'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U',
    'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
    'Я': 'IA', 'Ь': '', 'Ъ': '',
}
for i in (x := input()):
    if i.upper() in LITER:
        print(LITER[i.upper()].lower().capitalize() if i == i.upper() else LITER[i.upper()].lower(), end='')
    else:
        print(i, end='')

# K

people = []

for _ in range(int(input())):
    people.append(input())
    
print(len([i for i in people if people.count(i) > 1]))

# L

people = []
for _ in range(int(input())):
    people.append(input())
people = [i + ' - ' + str(people.count(i)) for i in set(people) if people.count(i) > 1]
if people:
    for x in sorted(people):
        print(x)
else:
    print('Однофамильцев нет')

# M

menu, new_menu = set(), set()

for _ in range(int(input())):
    menu.add(input())

for _ in range(int(input())):
    for j in range(int(input())):
        new_menu.add(input())

diff = sorted(menu - new_menu)

if diff:
    for dish in diff:
        print(dish)
else:
    print('Готовить нечего')

# N

ingredients, dishes = [], set()

for _ in range(int(input())):
    ingredients.append(input())

for _ in range(int(input())):
    dishes.add(x := input())
    for i in range(int(input())):
        if input() not in ingredients:
            dishes.discard(x)
            
if dishes:
    for dish in sorted(dishes):
        print(dish)
else:
    print('Готовить нечего')

# O

data = []
for i in list(map(lambda x: bin(int(x))[2:], input().split())):
    data.append({"digits": len(i),
                 "units": i.count('1'),
                 "zeros": i.count('0')})
print(data)

# P

near = set()
while x := input().split():
    for ind, i in enumerate(x):
        if i == 'зайка' and ind not in (0, len(x) - 1):
            near.add(x[ind - 1])
            near.add(x[ind + 1])
        elif i == 'зайка' and not ind:
            near.add(x[ind + 1])
        elif i == 'зайка' and ind == len(x) - 1:
            near.add(x[ind - 1])
for item in near:
    print(item)

# Q

friends = {}
while x := input().split():
    if x[0] not in friends:
        friends[x[0]] = {x[1]}
    else:
        friends[x[0]].add(x[1])
    if x[1] not in friends:
        friends[x[1]] = {x[0]}
    else:
        friends[x[1]].add(x[0])
friends_2 = dict.fromkeys(friends, set())
for friend in friends:
    for n in friends[friend]:
        friends_2[friend] = friends_2[friend].union(friends[n])
    friends_2[friend].discard(friend)
    for z in friends[friend]:
        friends_2[friend].discard(z)
data = []
for friend in friends_2:
    data.append(f'{friend}: {", ".join(sorted(friends_2[friend]))}')
data.sort()
for string in data:
    print(string)

# R

d = {}
for _ in range(int(input())):
    x = input().split()
    if not (z := f'{x[0][:-1]}-{x[1][:-1]}') in d:
        d[z] = 1
    else:
        d[z] += 1
print(max(d.values()))

# S

data = []
for _ in range(int(input())):
    k = list(map(lambda x: x.rstrip(','), input().split()))
    data.extend(set(k[1:]))
data = sorted(toy for toy in data if data.count(toy) == 1)
for kid in data:
    print(kid)

# T

data = sorted(map(int, input().split('; ')))
result = dict.fromkeys(data)
for i in data:
    for j in data:
        a, b = i, j
        while b:
            a, b = b, a % b
        if a == 1:
            if result[i]:
                result[i].add(j)
            else:
                result[i] = {j}
for number in result:
    if result[number]:
        print(f'{number} - {", ".join(map(str, sorted(result[number])))}')