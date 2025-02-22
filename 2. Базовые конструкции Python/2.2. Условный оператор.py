# A

name = input()
status = input()

print('Как Вас зовут?')
print(f'Здравствуйте, {name}!')
print('Как дела?')

if status == 'плохо':
    print('Всё наладится!')
else:
    print('Я за вас рада!')

# B

S = 43872
Pety = int(input())
Vasa = int(input())

Vp = S / Pety
Vv = S / Vasa

if Vp < Vv:
    print('Петя')
else:
    print('Вася')

# C

S = 43872

P = int(input())
V = int(input())
T = int(input())

if P > V and P > T:
    print('Петя')
elif V > T and V > P:
    print('Вася')
else:
    print('Толя')

# D

name1 = "Петя"
speed1 = int(input())
name2 = 'Вася' 
speed2 = int(input())
name3 = "Толя"
speed3 = int(input())

if speed1 < speed2:
    speed1, speed2 = speed2, speed1
    name1, name2 = name2, name1
elif speed2 < speed3:
    speed2, speed3 = speed3, speed2
    name2, name3 = name3, name2

if speed1 < speed2:
    speed1, speed2 = speed2, speed1
    name1, name2 = name2, name1

if speed2 < speed3:
    speed2, speed3 = speed3, speed2
    name2, name3 = name3, name2

if speed1 < speed2:
    speed1, speed2 = speed2, speed1
    name1, name2 = name2, name1
    
print(f'1. {name1}')
print(f'2. {name2}')
print(f'3. {name3}')

# E

N = int(input())
M = int(input())

P = 7
V = 6

P = P - 3 + 2 + N
V = V + 3 + 5 - 2 + M

if P > V:
    print('Петя')
else:
    print('Вася')

# F

year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print('YES')
else:
    print('NO')

# G

num = input()

if num == num[::-1]:
    print('YES')
else:
    print('NO')

# H

s = input()

if 'зайка' in s:
    print('YES')
else:
    print('NO')
    
# или

s = input()
print('YES' if 'зайка' in s else 'NO')
    
# I

name1 = input()
name2 = input()
name3 = input()

if (name1 < name2) and (name1 < name3):
    print(name1)
elif (name2 < name1) and (name2 < name3):
    print(name2)
else:
    print(name3)

# J

num = int(input())

sot = num // 100 % 10
des = num // 10 % 10
ed = num % 10

sh1 = des + ed
sh2 = sot + des

if sh1 > sh2:
    print(str(sh1) + str(sh2))
else:
    print(str(sh2) + str(sh1))

# K

num = input()

numlist = [int(num[0]), int(num[1]), int(num[2])]
numlist.sort()

if numlist[0] + numlist[2] == numlist[1] * 2:
    print('YES')
else:
    print('NO')

# L

side_1 = int(input())
side_2 = int(input())
side_3 = int(input())

check_1 = (side_1, side_2 + side_3)
check_2 = (side_2, side_1 + side_3)
check_3 = (side_3, side_1 + side_2)

if all(check[0] < check[1] for check in (check_1, check_2, check_3)):
    print('YES')
else:
    print('NO')

# M

elf = input()
gnome = input()
human = input()

if all(elf[0] in num for num in (elf, gnome, human)):
    print(elf[0])
elif all(elf[1] in num for num in (elf, gnome, human)):
    print(elf[1])
else:
    print('NO')

# N

from itertools import combinations

digits = input()

digitlist = []

for num_1, num_2 in list(combinations(digits, 2)):
    first = int(num_1 + num_2)
    second = int(num_2 + num_1)
    for num in (first, second):
        if num >= 10:
            digitlist.append(num)

digitlist.sort()

print(digitlist[0], digitlist[-1])

# O

num_1 = input()
num_2 = input()
nums = [int(n) for n in list(num_1 + num_2)]
nums.sort()
result = int(f'{nums[-1]}{(nums[1] + nums[2]) % 10}{nums[0]}')
print(result)

# P

name1 = 'Петя'
V1 = int(input())
name2 = 'Вася'
V2 = int(input())
name3 = 'Толя'
V3 = int(input())

if V1 < V2:
    V1, V2 = V2, V1
    name1, name2 = name2, name1
elif V2 < V3:
    V2, V3 = V3, V2
    name2, name3 = name3, name2

if V1 < V2:
    V1, V2 = V2, V1
    name1, name2 = name2, name1
elif V2 < V3:
    V2, V3 = V3, V2
    name2, name3 = name3, name2

if V1 < V2:
    V1, V2 = V2, V1
    name1, name2 = name2, name1
elif V2 < V3:
    V2, V3 = V3, V2
    name2, name3 = name3, name2

print(f'''{'':^8}{name1:^8}{'':^8}
{name2:^8}{'':^8}{'':^8}
{'':^8}{'':^8}{name3:^8}
{'II':^8}{'I':^8}{'III':^8}''')

# Q

def roots(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return 'Infinite solutions'
    elif a == 0 and b == 0:
        return 'No solution'
    elif a == 0:
        x = -c / b
        return f'{x:.2f}'
    d = b ** 2 - 4 * a * c
    if d > 0:
        x = [None, None]
        x[0] = (-b + d ** 0.5) / (2 * a)
        x[1] = (-b - d ** 0.5) / (2 * a)
        x.sort()
        return f'{x[0]:.2f} {x[1]:.2f}'
    elif d == 0:
        x = -b / (2 * a)
        return f'{x:.2f}'
    return 'No solution'


a = float(input())
b = float(input())
c = float(input())
print(roots(a, b, c))

# R

a = int(input())
b = int(input())
c = int(input())

abc_list = [a, b, c]
abc_list = sorted(abc_list)

a = abc_list[0]
b = abc_list[1]
c = abc_list[2]

if a**2 + b**2 == c**2:
    print('100%')
elif a**2 + b**2 < c**2:
    print('велика')
else:
    print('крайне мала')

# S

x = float(input())
y = float(input())

sea = (x ** 2 + y ** 2) ** 0.5 > 10

in_danger = (
    (x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5) or  
    (-4 <= x < 0 and 5 >= y >= 0) or                    
    (-7 <= x < -4 and 5 >= y >= 0 and 5 * x - 3 * y > -35) or         
    (0.25 * x ** 2 + 0.5 * x - 8.75 <= y <= 0)       
)

if sea:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif in_danger:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# T

places = [input(), input(), input()]
places.sort()
for place in places:
    if 'зайка' in place:
        print(place, len(place))
        break