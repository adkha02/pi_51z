m = int(input())
available = set()
for _ in range(m):
    available.add(input())
n = int(input())
cooked = set()
for _ in range(n):
    for dish in input().split():
        cooked.add(dish)
not_cooked = available - cooked
for dish in not_cooked:
    print(dish)
