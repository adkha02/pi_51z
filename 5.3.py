list1 = set()
while True:
    s = input()
    if s == "":
        break
    list1.add(int(s))

list2 = set()
while True:
    s = input()
    if s == "":
        break
    list2.add(int(s))

common = list1 & list2
if common:
    print(*common)
else:
    print("EMPTY")
