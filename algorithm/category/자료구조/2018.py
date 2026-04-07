N = int(input())

i = j = 1

temp = 1

answer = 0
while i <= j and i <= N and j <= N:
    if temp < N:
        j += 1
        temp += j
    elif temp > N:
        temp -= i
        i += 1
    else:
        answer += 1
        j += 1
        temp += j


print(answer)
