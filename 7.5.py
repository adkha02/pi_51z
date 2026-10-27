n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
result = [x * 3 for x in nums]
print(*result)
