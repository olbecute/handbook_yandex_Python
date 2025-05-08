# A

def print_hello(name):
    print(f"Hello, {name}!")

# B

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# C

def number_length(num):
    num = int(num)
    return len(str(abs(num)))

# D

def month(month_number, language):
    months_ru = [
        'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
        'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
    ]
    months_en = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    
    if language == "ru":
        return months_ru[month_number - 1]
    elif language == "en":
        return months_en[month_number - 1]
    else:
        return ""

# E

def split_numbers(s):
    s = tuple(map(int, s.split()))
    return s

# F

def modern_print(text, _printed=set()):
    if text not in _printed:
        print(text)
        _printed.add(text)

# G

def can_eat(knight_pos, figure_pos):
    x1, y1 = knight_pos
    x2, y2 = figure_pos
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

# H

def is_palindrome(obj):
    if isinstance(obj, int):
        s = str(obj)
        return s == s[::-1]
    else:
        return obj == obj[::-1]
    
# I

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

# J

def merge(tuple1, tuple2):
    merged = []
    i = j = 0
    len1, len2 = len(tuple1), len(tuple2)
    
    while i < len1 and j < len2:
        if tuple1[i] < tuple2[j]:
            merged.append(tuple1[i])
            i += 1
        else:
            merged.append(tuple2[j])
            j += 1
    
    merged.extend(tuple1[i:])
    merged.extend(tuple2[j:])
    
    return tuple(merged)
