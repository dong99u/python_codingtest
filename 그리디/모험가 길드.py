n = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

index = 0

count = 0
while index < n:
    count += 1
    index += arr[index]

print(count)