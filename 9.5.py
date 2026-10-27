words = input().split()
formatted = [f'"{w}"' for w in words]
print("[" + ", ".join(formatted) + "]")
