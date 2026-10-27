n = int(input())
lines = [input() for _ in range(n)]
res = [line for line in lines if "лук" not in line]
print(", ".join(res))
