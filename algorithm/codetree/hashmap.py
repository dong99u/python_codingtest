import heapq

n = int(input())
arr = list(map(int, input().split()))

sum_val = arr[-1]
max_avg_val = 0
hq = [arr[-1]]

for i in range(n - 2, 0, -1):
    heapq.heappush(hq, arr[i])
    sum_val += arr[i]
    min_num = hq[0]
    avg = (sum_val - min_num) / (n - i - 1)
    if max_avg_val < avg:
        max_avg_val = avg

print(f'{max_avg_val:.2f}')