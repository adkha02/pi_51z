m = int(input())
eng = set()
for _ in range(m):
    eng.add(input())
n = int(input())
ger = set()
for _ in range(n):
    ger.add(input())
only_one = eng ^ ger
if only_one:
    print(len(only_one))
else:
    print("NO")
