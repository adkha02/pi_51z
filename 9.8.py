url = input()
parts = url.split('?')[1].split('&')
for part in parts:
    if part.startswith('q='):
        print(part[2:])
        break
