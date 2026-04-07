answer = 0
A = list(map(str, input().split('-')))

def sum_numbers(strs):
    sum = 0
    temp = strs.split('+')
    for i in temp:
        sum += int(i)

    return sum

for i in range(len(A)):
    temp = sum_numbers(A[i])

    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)