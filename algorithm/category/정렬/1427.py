n = list(input())
k = len(n)

for i in range(k - 1):
    max_idx = i

    # 최댓값 찾기
    for j in range(i + 1, k):
        if n[max_idx] < n[j]:
            max_idx = j

    n[i], n[max_idx] = n[max_idx], n[i]

for x in n:
    print(x, end='')
