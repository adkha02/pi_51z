n = int(input())
surnames = []
for _ in range(n):
    surnames.append(input())
from collections import Counter
counts = Counter(surnames)
total = 0
for surname, count in counts.items():
    if count > 1:
        total += count
print(total)
