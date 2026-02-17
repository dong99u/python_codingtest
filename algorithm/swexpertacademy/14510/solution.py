import sys
sys.stdin = open('input.txt')

t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    heights = list(map(int, input().split()))

    max_height = max(heights)
    heights = [(max_height - h) for h in heights if h != max_height]

    left_count = len(heights)
    days = 0


    '''
    매번 heights를 돌면서 다음의 규칙을 적용함
    1. 홀수 height가 존재하면 홀수 날에 홀수만큼 남은 나무 우선 선택
    2. 짝수 날에는 우선적으로 짝수만큼 남은 나무 우선 선택
    3. 홀수 height가 없으면 height 홀수 날에 height > 2 라면 선택
    '''
    while left_count > 0:
        days += 1

        # 홀수 존재 여부
        is_odd_exist = any([height % 2 for height in heights])
        for i in range(len(heights)):
            # 0이면 패스
            if heights[i] == 0:
                continue

            # 홀수 날에는 홀수만큼 남은 나무 우선 선택
            if is_odd_exist and days % 2 and heights[i] % 2:
                heights[i] -= 1
                if heights[i] == 0:
                    left_count -= 1
                break
            # 짝수 날에는 짝수만큼 남은 나무 우선 선택
            elif days % 2 == 0 and heights[i] % 2 == 0:
                heights[i] -= 2
                if heights[i] == 0:
                    left_count -= 1
                break
            elif not is_odd_exist and days % 2 and heights[i] > 2:
                heights[i] -= 1
                if heights[i] == 0:
                    left_count -= 1
                break

    print(f'#{test_case} {days}')

