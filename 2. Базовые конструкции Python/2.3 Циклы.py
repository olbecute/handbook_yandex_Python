# A

while (s := input()) != 'Три!':
    print('Режим ожидания...')
else:
    print("Ёлочка, гори!")

# B

count = 0

while (s := input()) != 'Приехали!':
    if "зайка" in s:  
        count += 1
    else:
        continue

print(count)

# C

a = int(input())
b = int(input())
num_list = []

for i in range(a, b + 1):
    num_list.append(i)

result = " ".join(map(str, num_list))
print(result)

# D

a, b = int(input()), int(input())
if a < b:
    for i in range(a, b + 1):
        print(i, end=' ')
else:
    for i in range(a, b - 1, -1):
        print(i, end=' ')

# E

sum = 0

while (n := float(input())) != 0:
    if n >= 500:
        sum += 0.9 * n
    else:
        sum += n

print(sum)

# F

a, b = int(input()), int(input())
while b:
    a, b = b, a % b
print(a)

# G

a, b = c, d = int(input()), int(input())
while b:
    a, b = b, a % b
print(c * d // a)

# H

s = input()
num = int(input())

for _ in range(num):
    print(s)
    
# I

num = int(input())
f = 1

for i in range(1, num):
    f *= i

print(num)

# J

x, y = 0, 0

while (direction := input()) != 'СТОП':
    n = int(input())
    if direction == 'ВОСТОК':
        x += n
    elif direction == 'ЗАПАД':
        x -= n
    elif direction == 'СЕВЕР':
        y += n
    elif direction == 'ЮГ':
        y -= n
    
print(y, x, sep='\n')

# K

print(sum(map(int, input())))

# L

print(max(map(int, input())))

# M

n, first = int(input()), input()

for _ in range(n - 1):
    first = min(first, input())
    
print(first)

# N

n = int(input())

i, result = 2, 'YES'

if n > 1:
    while n % i:
        if i > n ** 0.5:
            break
        i += 1
    else:
        result = 'NO'
else:
    result = 'NO'

print(result)

# O

counter = 0

for _ in range(int(input())):
    if 'зайка' in input():
        counter += 1
        
print(counter)

# P

print('YES') if (x := input()) == x[::-1] else print('NO')

# Q

print(''.join(filter(lambda x: int(x) % 2, input())))

# R

n, result, i = int(input()), [], 1

if n < 2:
    print(n)
while n > 1:
    i += 1
    if not n % i:
        result.append(str(i))
        n //= i
        i = 1
else:
    print(' * '.join(result))

# S

begin, end = 1, 1001

print((begin + end) // 2)

while (x := input()) != 'Угадал!':
    if x == 'Меньше':
        end = (begin + end) // 2
        print((begin + end) // 2)
    elif x == 'Больше':
        begin = (begin + end) // 2
        print((begin + end) // 2)
print('=' * 35)

# T

result, hn1 = -1, 0
for i in range(int(input())):
    b = int(input())
    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    t = ((m + r + hn1) * 37) % 256
    if t != h or h > 99:
        result = i
        break
    hn1 = h
print(result)