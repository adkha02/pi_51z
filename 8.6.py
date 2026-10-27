n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for i in range(n):
    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
for x in nums:
    print(x)
