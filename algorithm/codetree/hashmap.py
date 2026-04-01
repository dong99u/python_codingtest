import sys
input = sys.stdin.readline

n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

d = {}

for command in commands:
    if command[0] == 'add':
        c, k, v = command
        d[k] = v
    elif command[0] == 'remove':
        c, k = command
        del d[k]
    else:
        c, k = command
        print(d[k] if k in d else None)