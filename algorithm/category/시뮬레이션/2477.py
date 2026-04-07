n = int(input())
arr = []
for _ in range(6):
    dir_num, length = map(int, input().split())
    arr.append((dir_num, length))

# 가장 긴 가로와 세로 찾기
max_width_idx = max(range(6), key=lambda i: arr[i][1] if arr[i][0] in (1, 2) else 0)
max_height_idx = max(range(6), key=lambda i: arr[i][1] if arr[i][0] in (3, 4) else 0)

max_width = arr[max_width_idx][1]
max_height = arr[max_height_idx][1]

# 파인 부분의 변 = 가장 긴 변의 정반대편 (인덱스 +3)
small_width = arr[(max_height_idx + 3) % 6][1]
small_height = arr[(max_width_idx + 3) % 6][1]

# 넓이 계산
big_area = max_width * max_height
small_area = small_width * small_height

print((big_area - small_area) * n)