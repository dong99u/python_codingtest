import sys, heapq
input = sys.stdin.readline

hq = []

n = int(input())

for _ in range(n):
    num = int(input())

    if num == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (abs(num), num))