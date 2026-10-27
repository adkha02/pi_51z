n = int(input())
word = [""] * n
for _ in range(n):
    parts = input().split()
    pos = int(parts[0])
    letter = parts[1]
    word[pos - 1] = letter
print("".join(word))
