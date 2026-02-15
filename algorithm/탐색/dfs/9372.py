import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    for _ in range(m):
        input()  # 간선 정보는 읽기만 함

    print(n - 1)