nums = list(map(int, input().split()))
res = [x**2 for x in nums if x % 2 != 0 and str(x**2)[-1] != '9']
print(*res)
