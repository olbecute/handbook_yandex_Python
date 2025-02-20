# A

print('Привет, Яндекс!')

# B

name = input()
print('Как Вас зовут?')
print('Привет,', name)

# C

s = input()
print(s)
print(s)
print(s)

# D

m = 2.5
c = 38
s = 95
a = int(input())
r = a - s
print(r)

# E

cena1 = int(input())
m = int(input())
dengi = int(input())
sdacha = dengi - cena1 * m
print(sdacha)

# F

name = input()
cena1 = int(input())
ves = int(input())
itog = cena1 * ves
vneseno = int(input())
sdacha = vneseno - itog

print('Чек')
print(f'{name} - {ves}кг - {cena1}руб/кг')
print(f'Итого: {itog}руб')
print(f'Внесено: {vneseno}руб')
print(f'Сдача: {sdacha}руб')

# G

n = int(input())

for _ in range(n):
    print('Купи слона!')

# H

n = int(input())
s = input()

for _ in range(n):
    print(f'Я больше никогда не буду писать "{s}"!')
    
# I

n = int(input())
m = int(input())
r = (n * m) * 0.5
print(int(r))

# J

name = input()
num = input()

list_num = list(num)

group = list_num[0]
n = list_num[2]
bed = list_num[1]

print(f'Группа №{group}.')
print(f'{n}. {name}.')
print(f'Шкафчик: {num}.')
print(f'Кроватка: {bed}.')

# K

abcd = int(input())

a = abcd // 1000 % 10
b = abcd // 100 % 10
c = abcd // 10 % 10
d = abcd // 1 % 10

badc = str(b) + str(a) + str(d) + str(c)

print(badc)

# L

n1 = int(input())
n2 = int(input())

n1_a = n1 % 10
n1_b = (n1 // 10) % 10
n1_c = (n1 // 100) % 10

n2_a = n2 % 10
n2_b = (n2 // 10) % 10
n2_c = (n2 // 100) % 10

a = (n1_a + n2_a) % 10
b = (n1_b + n2_b) % 10
c = (n1_c + n2_c) % 10

res = c * 100 + b * 10 + a

print(res)

# M

b = int(input())
c = int(input())

b1 = c // b

print(b1)
print(c - (b1 * b))

# N

red = int(input())
green = int(input())
blue = int(input())

n = red + blue + 1

print(n)

# O

N = int(input())
M = int(input())
T = int(input())

min_start = N * 60 + M
delivery = min_start + T
delivery %= 1440

hours = delivery // 60
minets = delivery % 60

print(f'{hours:02}:{minets:02}')

# P

A = int(input())
B = int(input())
V = int(input())

S = abs(B - A)
t = S / V

print(round(t, 2))

# Q

num10 = int(input(), 10)
num2 = int(input(), 2)

print(num10 + num2)

# R

cena = int(input(), 2)
kupura = int(input()) 

print(kupura - cena)


# S

name = input()
cena = int(input())
ves = int(input())
dengi = int(input())

itog = cena * ves
sdacha = dengi - itog

cena_str = f"{ves}кг * {cena}руб/кг"
itog_str = f"{itog}руб"
dengi_str = f"{dengi}руб"
sdacha_str = f"{sdacha}руб"

print(f"{'Чек':=^35}")
print(f"Товар:{name:>29}")
print(f"Цена:{cena_str:>30}")
print(f"Итого:{itog_str:>29}")
print(f"Внесено:{dengi_str:>27}")
print(f"Сдача:{sdacha_str:>29}")
print("=" * 35)

# T

N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())

if K1 < K2:
    K1, K2 = K2, K1
else:
    continue

x = N * (M - K2)
x = x / (K1 - K2)
y = N - x

x = int(x)
y = int(y)
print(x, y)