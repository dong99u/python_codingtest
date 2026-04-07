n = int(input())
arr = []

for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x: (x[1], x[0]))
count = 0
end = -1

for i in range(n):
    if arr[i][0] >= end:
        end = arr[i][1]
        count += 1

print(count)