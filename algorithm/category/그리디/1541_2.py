import sys
input = sys.stdin.readline

strs = input().rstrip()

arr = strs.split('-')

answer = sum(list(map(int, arr[0].split('+'))))

for exp in arr[1:]:
    answer -= sum(list(map(int, exp.split('+'))))

print(answer)



