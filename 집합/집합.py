import sys
input = sys.stdin.readline  # 빠른 입력을 위해

M = int(input())

result = set()
for _ in range(M):
    # 입력을 먼저 split하여 명령어와 값을 분리
    command = input().split()

    # 명령어는 항상 첫 번째 원소
    inst = command[0]

    # 값이 필요한 명령어인 경우에만 값을 가져옴
    if len(command) > 1:
        val = int(command[1])

    if inst == 'add':
        result.add(val)
    elif inst == 'remove':
        # discard()는 원소가 없어도 에러를 발생시키지 않음
        result.discard(val)
    elif inst == 'check':
        if val in result:
            print(1)
        else:
            print(0)
    elif inst == 'toggle':
        if val in result:
            result.discard(val)  # remove 대신 discard 사용
        else:
            result.add(val)
    elif inst == 'all':
        result = set(range(1, 21))  # 더 간결한 표현
    elif inst == 'empty':
        result = set()