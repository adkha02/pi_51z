n = int(input())
pairs = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    grade = int(parts[1])
    pairs.append((name, grade))
for name, grade in pairs:
    print(f"{name} {grade}")
print()
for name, grade in pairs:
    if grade == 4 or grade == 5:
        print(f"{name} {grade}")
