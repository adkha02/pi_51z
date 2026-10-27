shift = int(input())
text = input()
lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
result = []
for c in text:
    if c in lower_alphabet:
        idx = lower_alphabet.index(c)
        result.append(lower_alphabet[(idx + shift) % 33])
    elif c in upper_alphabet:
        idx = upper_alphabet.index(c)
        result.append(upper_alphabet[(idx + shift) % 33])
    else:
        result.append(c)
print("".join(result))
