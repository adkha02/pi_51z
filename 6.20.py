username = input()
valid = True
for c in username:
    if not (c.isalpha() and c.isascii() or c.isdigit() or c == "_"):
        print(f"Неверный символ: {c}")
        valid = False
        break
if valid:
    print("OK")
