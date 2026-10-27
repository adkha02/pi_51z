from collections import Counter
word1 = input()
word2 = input()
bulls = sum(1 for a, b in zip(word1, word2) if a == b)
c1 = Counter(word1)
c2 = Counter(word2)
common = sum((c1 & c2).values())
cows = common - bulls
print(f"Быки: {bulls}")
print(f"Коровы: {cows}")
