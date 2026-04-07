def solution(cap, n, deliveries, pickups):
    answer = 0

    # 뒤에서부터 누적량 계산
    deliver = 0  # 아직 배달 못한 택배
    pickup = 0   # 아직 수거 못한 택배

    # 가장 먼 집부터 확인
    for i in range(n - 1, -1, -1):
        deliver += deliveries[i]
        pickup += pickups[i]

        # 이 집까지 가야 하는 왕복 횟수
        while deliver > 0 or pickup > 0:
            # 한 번 왕복 (i+1은 인덱스 0부터 시작이므로 실제 거리)
            answer += (i + 1) * 2

            # 트럭 용량만큼 처리
            deliver -= cap
            pickup -= cap

    return answer

if __name__ == '__main__':
    print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
    print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))