import sys
input = lambda: sys.stdin.readline().rstrip()

def search(active, max_count):
    if not active:
        return 0

    left, right = 0, active[-1] - active[0]
    while left < right:
        mid = (left + right) // 2
        # 그리디: mid 시간 안에 max_count 마리로 커버 가능한지
        count = 1
        start = active[0]
        for pos in active[1:]:
            if pos - start > mid:
                count += 1
                start = pos
        if count <= max_count:
            right = mid
        else:
            left = mid + 1
    return left

Q = int(input())
arr = [0]  # arr[0] = 여왕개미집, arr[i] = i번 개미집 좌표 (-1이면 철거됨)

for _ in range(Q):
    command, *data = map(int, input().split())

    if command == 100:   # 마을 건설
        n, *positions = data
        arr += positions
    elif command == 200: # 개미집 추가
        arr.append(data[0])
    elif command == 300: # 개미집 철거
        arr[data[0]] = -1
    elif command == 400: # 정찰
        # 활성 개미집만 추출 (여왕개미집 제외, 이미 정렬됨)
        active = [arr[i] for i in range(1, len(arr)) if arr[i] != -1]
        print(search(active, data[0]))