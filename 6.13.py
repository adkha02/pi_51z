s = input()
if s.startswith("Не") or s.startswith("не"):
    print(s[2:])
else:
    print(s)
