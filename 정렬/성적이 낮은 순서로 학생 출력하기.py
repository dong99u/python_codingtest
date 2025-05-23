from collections import defaultdict

n = int(input())

d = defaultdict(int)
for _ in range(n):
    name, score = input().split()
    d[name] = score

print(sorted(d.keys(), key=lambda name: d[name]))

