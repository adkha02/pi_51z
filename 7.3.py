n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
sums = []
for i in range(n - 1):
    sums.append(nums[i] + nums[i + 1])
print(*sums)
