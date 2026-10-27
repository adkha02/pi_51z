n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
last = nums[-1]
rest = nums[:-1]
found = False
for i in range(len(rest)):
    for j in range(i + 1, len(rest)):
        if rest[i] * rest[j] == last:
            found = True
            break
    if found:
        break
print("ДА" if found else "НЕТ")
