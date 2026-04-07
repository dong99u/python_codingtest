import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(input().rstrip())

arr = list(set(arr))

arr.sort(key=lambda x: (len(x), x))

for word in arr:
    print(word)