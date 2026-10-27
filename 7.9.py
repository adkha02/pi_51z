white = []
while True:
    s = input()
    if s == "":
        break
    white.append(s)
queries = []
while True:
    s = input()
    if s == "":
        break
    queries.append(s)
white_set = set(white)
for q in queries:
    if q in white_set:
        print(q)
