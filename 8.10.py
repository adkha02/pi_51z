n = int(input())
lst = []
for _ in range(n):
    s = input()
    lst.append((len(s), s))
for t in lst:
    print(t)
