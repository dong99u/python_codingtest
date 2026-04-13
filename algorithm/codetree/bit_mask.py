n = int(input())
arr = list(map(int, input().split()))

result = 0

# 1단계: 가능한 모든 (a, b) 쌍을 미리 계산
pairs = []
for i in range(n):
    for j in range(i + 1, n):
        a, b = arr[i], arr[j]
        # a, b끼리 겹치지 않는 쌍만 저장
        if a & b == 0:
            pairs.append((a | b, a + b))  # (합쳐진 비트, 합계)

# 2단계: 각 쌍에 대해 세 번째 수 c를 탐색
for combined, pair_sum in pairs:
    for c in arr:
        # c가 (a, b) 쌍과 비트가 전혀 겹치지 않으면
        if combined & c == 0:
            result = max(result, pair_sum + c)

print(result)