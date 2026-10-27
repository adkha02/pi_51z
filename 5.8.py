m = int(input())
products = set()
for _ in range(m):
    products.add(input())
n = int(input())
for _ in range(n):
    parts = input().split()
    name = parts[0]
    ingredients = set(parts[1:])
    if ingredients.issubset(products):
        print(name)
