# A

[i ** 2 for i in range(a, b + 1)]

# B

[[j * i for j in range(1, n + 1)] for i in range(1, n + 1)]

# C

[len(word) for word in sentence.split(' ')]

# D

{n for n in numbers if n % 2 != 0}

# E

{number for number in numbers if number in [i ** 2 for i in range(1, int(max(numbers) ** 0.5 + 1))]}

# F

{letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}

# G

{number: [i for i in range(1, number + 1) if not number % i] for number in numbers}

# H

''.join(word[0] for word in string.split()).upper()
    
# I

' - '.join(str(i) for i in sorted(set(numbers)))

# J

''.join(i * j for i, j in rle)
