import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

for _ in range(k):
    gender, switch_num = map(int, input().split())

    if gender == 1:
        for i in range(switch_num - 1, n, switch_num):
            arr[i] = 1 - arr[i]

    else:
        idx = switch_num - 1

        left, right = idx - 1, idx + 1
        while left >= 0 and right < n and arr[left] == arr[right]:
            left -= 1
            right += 1

        # 2단계: 찾은 구간 전체 토글 (중간 포함!)
        for i in range(left + 1, right):
            arr[i] = 1 - arr[i]


for i in range(n):
    print(arr[i], end=' ')
    if (i + 1) % 20 == 0:  # 20개마다 줄바꿈
        print()

if n % 20 != 0:
    print()