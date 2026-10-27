n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
for s in sorted(lst, key=lambda x: (len(x), x)):
    print(s)
