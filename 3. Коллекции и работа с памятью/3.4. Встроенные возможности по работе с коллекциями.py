# A

input_string = input().strip()
words = input_string.split()

for i, word in enumerate(words, start=1):
    print(f"{i}. {word}")

# B

line1 = input().strip().split(', ')
line2 = input().strip().split(', ')

min_length = min(len(line1), len(line2))

for i in range(min_length):
    print(f"{line1[i]} - {line2[i]}")

# C

start, end, step = map(float, input().split())

current = start
while current <= end + 1e-9: 
    print(f"{current:.2f}")
    current = round(current + step, 10)  

# D

from itertools import accumulate

words = input().split()

for phrase in accumulate(words, lambda x, y: f"{x} {y}"):
    print(phrase)

# E

from itertools import chain

products = chain(*(input().strip().split(', ') for _ in range(3)))

for i, product in enumerate(sorted(products), 1):
    print(f"{i}. {product}")

# F

from itertools import product

suits_order = ['пик', 'треф', 'бубен', 'червей']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

excluded_suit = input().strip()

suits = [suit for suit in suits_order if suit != excluded_suit]

deck = []
for rank, suit in product(ranks, suits):
    deck.append(f"{rank} {suit}")

for card in deck:
    print(card)

# G

n = int(input())
players = [input().strip() for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        print(f"{players[i]} - {players[j]}")

# H

from itertools import islice

M = int(input())
menu = [input().strip() for _ in range(M)]

N = int(input())

for day in range(N):
    print(menu[day % M])
    
# I

import itertools

n = int(input())
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        row.append(str(i * j))
    print(' '.join(row))

# J

n = int(input())
print("А Б В")

import itertools

for a, b in itertools.product(range(1, n), range(1, n)):
    c = n - a - b
    if c >= 1:
        print(f"{a} {b} {c}")           

# K

import itertools

N = int(input())
M = int(input())

max_num = N * M
width = len(str(max_num))

for i in range(1, N + 1):
    row = []
    for j in range(1, M + 1):
        num = (i - 1) * M + j
        row.append(f"{num:>{width}}")
    print(' '.join(row))

# L

items = []
for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for i, item in enumerate(sorted(items), start=1):
    print(f'{i}. {item}')

# M

import itertools

n = int(input())
names = [input().strip() for _ in range(n)]

permutations = sorted(itertools.permutations(names))

for perm in permutations:
    print(', '.join(perm))

# N

from itertools import permutations

items = []

for _ in range(int(input())):
    items.append(input())

for i in sorted(permutations(items, 3)):
    print(', '.join(i))

# O

from itertools import permutations

items = []

for _ in range(int(input())):
    items.extend([item for item in input().split(', ')])
for item in sorted(permutations(items, 3)):
    print(' '.join(item))

# P

from itertools import product, permutations

suits_ro = ["бубен", "пик", "треф", "червей"]
nominal = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

suit, exception = input(), input()
best_suit = [s for s in suits_ro if s.startswith(suit[0:3])][0]

nominal.remove(exception)
comb = permutations(product(sorted(nominal), sorted(suits_ro)), 3)
y = [', '.join(' '.join(j) for j in sorted(i)) for i in comb]
triads = [i for i in y if best_suit in i][:10]
for triad in triads:
    print(triad)

# Q

from itertools import product, permutations

suits_ro = sorted(["бубен", "пик", "треф", "червей"])
suit, exception, situation = input(), input(), input()
best_suit = [s for s in suits_ro if s.startswith(suit[0:3])][0]
nominal = sorted(["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"])
nominal.remove(exception)
comb = permutations(product(nominal, suits_ro), 3)
y = sorted(set([', '.join(' '.join(j) for j in sorted(i)) for i in comb]))
triads = [i for i in y if best_suit in i]
for ind, triad in enumerate(triads):
    if triad == situation:
        print(triads[ind + 1])
        break

# R

x = input()
print('a b c f')
for i in range(8):
    values = list(bin(i)[2:].zfill(3))
    a, b, c = map(int, values)
    print(' '.join(values), int(eval(x)))

# S

x = input()
args = sorted({i for i in x if i.isupper()})
print(' '.join(args), 'F')
for i in range(2 ** len(args)):
    values = list(bin(i)[2:].zfill(len(args)))
    exec(', '.join(args) + " = map(int, values)")
    print(' '.join(values), int(eval(x)))

# T

from itertools import product

OPERATORS = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

PRIORITY = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}


def postfix_expression(expression, variables):
    stack, result, lst = [], [], expression.split()
    for i in lst:
        if i in variables:
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(OPERATORS[stack.pop()])
            stack.pop()
        elif i in OPERATORS.keys():
            while len(stack) and PRIORITY[i] >= PRIORITY[stack[-1]]:
                result.append(OPERATORS[stack.pop()])
            stack.append(i)
    for _ in range(len(stack)):
        result.append(OPERATORS[stack.pop()])
    return result


def result_of_expression(postfix_exp, variables):
    stack = []
    for i in range(len(postfix_exp)):
        if postfix_exp[i] in variables.keys():
            stack.append(variables[postfix_exp[i]])
        else:
            if postfix_exp[i] == 'not':
                stack.append(not stack.pop())
            else:
                var2, var1 = stack.pop(), stack.pop()
                stack.append(eval(f'{var1} {postfix_exp[i]} {var2}'))
    return int(stack.pop())


statement = input()
var_all = sorted(set([i for i in statement if i.isupper()]))
print(' '.join(var_all), 'F')
table = product([0, 1], repeat=len(var_all))
statement = statement.replace('(', '( ').replace(')', ' )')
exp = postfix_expression(statement, var_all)

for row in table:
    res = {}
    for k, v in zip(var_all, row):
        res[k] = v
    print(' '.join(str(x) for x in row), result_of_expression(exp, res))