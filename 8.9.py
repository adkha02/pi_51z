n = int(input())
people = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    height = int(parts[1])
    people.append((name, height))
for name, height in sorted(people, key=lambda x: x[1], reverse=True):
    print(f"{name} {height}")
