import sys
input = sys.stdin.readline

MALE = 1
FEMALE = 2

switch_count = int(input())
switches = list(map(int, input().split()))
students_count = int(input())
students = [tuple(map(int, input().split())) for _ in range(students_count)]

for gender, num in students:
    if gender == MALE:
        for i in range(switch_count):
            if (i + 1) % num == 0:
                switches[i] = 1 - switches[i]

    elif gender == FEMALE:
        l = r = num - 1
        while 0 <= l - 1 and r < switch_count - 1:
            if switches[l - 1] == switches[r + 1]:
                l -= 1
                r += 1
            else:
                break
        for i in range(l, r + 1):
            switches[i] = 1 - switches[i]

for i in range(switch_count):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:  # 20개마다 줄바꿈
        print()

if switch_count % 20 != 0:
    print()