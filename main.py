import random

number = random.randint(3, 20)
print(f'The given number: {number}')
pairs = []
for a in range(1, 21):
    for b in range(1, 21):
        if (a + b) % number == 0:
            pairs.append((a, b))
print('Matching pairs of numbers:')
for pair in pairs:
    print(pair)

