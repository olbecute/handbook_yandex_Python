# A

for _ in range(int(input())):
    if (word := input())[0] not in 'абв':
        print('NO')
        break
else:
    print('YES')  

# B

for el in input():
    print(el)

# C

L = int(input())
N = int(input())

for i in range(N):
    s = input()
    if len(s) > L:
        print(f'{s[:L - 3]}...')
    else:
        print(s)

# D

while (n := input()):
    if not n.endswith('@@@'):
        if n.startswith('##'):
            print(n[2:])
        else:
            print(n)

# E

text = input()

if text == text[::-1]:
    print('YES')
else:
    print('NO')

# F

counter = 0

for _ in range(int(input())):
    counter += input().count("зайка")
    
print(counter)

# G

s = list(map(int, input().split()))
print(s[0] + s[1])


# H

for _ in range(int(input())):
    if "зайка" in (place := input()):
        print(place.index("зайка") + 1)
    else:
        print("Заек нет =(")
    
# I

while (line := input()):
    if not line:
        break
    comment_index = line.find('#')
    if comment_index == 0:
        continue
    elif comment_index != -1:
        line = line[:comment_index].rstrip()
    if line:
        print(line)

# J

data = []
while (n := input()) != 'ФИНИШ':
    data.extend(n.lower().split())
max_count, data = 0, ''.join(data)
for symbol in set(data):
    max_count = max(max_count, data.count(symbol))
print(min([i for i in set(data) if data.count(i) == max_count]))

# K

num = int(input())
text_list = []

for i in range(num):
    text_list.append(input())

poisk = input().lower()

for el in text_list:
    if poisk in el.lower():
        print(el)
    else:
        continue


# L

menu = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
days = int(input())

for i in range(days):
    print(menu[i % len(menu)])



# M

N = int(input())

numbers = []
for _ in range(N):
    num = int(input())  
    numbers.append(num)

P = int(input())

for num in numbers:
    print(num ** P)

# N

numbers = list(map(int, input().split()))

P = int(input())

result = [str(num ** P) for num in numbers]

print(" ".join(result))

# O

numbers = list(map(int, input().split()))

a = numbers[0]

while len(numbers) > 1:
    b = numbers[1]
    while b:
        a, b = b, a % b
    numbers.pop(1)
    
print(a)

# P

length, line = int(input()), []

for _ in range(int(input())):
    line.append(input())
    
for i in line:
    if length > 3:
        print(i[:length - 3] + "..." if len(i) >= length - 3 else (i + "..." if length == 4 else i))
        length -= len(i)

# Q

line = ''.join(input().lower().split())

print('YES' if line == line[::-1] else 'NO')

# R

s = input()

first = s[0]
count = 0

s = s + 'a'

for el in s:
    if first == el:
        count += 1
        first = el
    else:
        print(first, count)
        first = el
        count = 1

# S

s = list(input().split())
res = []
res.append(int(s[0]))

for el in s[1:]:
    if el.isdigit():
        res.append(int(el))
    else:
        a = res.pop()
        exec('res[-1]' + el + '= a')
print(res[0])

# T

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


data = list(input().split())
result = [int(data[0])]
for i in data[1:]:
    if i.isdigit():
        result.append(int(i))
    elif i == "/":
        a = result.pop()
        result[-1] //= a
    elif i == "~":
        result[-1] = -result[-1]
    elif i == "#":
        result.append(result[-1])
    elif i == "!":
        result[-1] = factorial(result[-1])
    elif i == "@":
        result.append(result.pop(-3))
    else:
        a = result.pop()
        exec("result[-1] " + i + "= a")
print(result[0])