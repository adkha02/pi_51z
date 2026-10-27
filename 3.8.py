n = int(input())
result = 1
for _ in range(n):
    x = int(input())
    if x != 0:
        result *= x
print(result)
