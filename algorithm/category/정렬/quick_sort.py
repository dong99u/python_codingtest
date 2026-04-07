def quick_sort(arr, left, right):
    """
    퀵 정렬 - 모든 로직이 하나의 함수에
    첫 번째 원소를 피벗으로, start/end 포인터 사용
    """
    # 기저 조건
    if left >= right:
        return

    # ===== 파티션 로직 시작 =====
    pivot = arr[left]  # 첫 번째 원소를 피벗으로
    start = left + 1   # start 포인터
    end = right        # end 포인터

    while True:
        # start: 피벗보다 큰 값을 찾을 때까지 오른쪽으로
        while start <= end and arr[start] <= pivot:
            start += 1

        # end: 피벗보다 작은 값을 찾을 때까지 왼쪽으로
        while start <= end and arr[end] >= pivot:
            end -= 1

        # start와 end가 교차하면 종료
        if start > end:
            break

        # 교환
        arr[start], arr[end] = arr[end], arr[start]

    # 피벗을 올바른 위치(end)로 이동
    arr[left], arr[end] = arr[end], arr[left]

    pivot_pos = end  # 피벗의 최종 위치
    # ===== 파티션 로직 끝 =====

    # 왼쪽 부분 재귀 정렬
    quick_sort(arr, left, pivot_pos - 1)

    # 오른쪽 부분 재귀 정렬
    quick_sort(arr, pivot_pos + 1, right)


# 사용 예시
arr = [5, 3, 8, 1, 2, 7, 4]
print("정렬 전:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("정렬 후:", arr)