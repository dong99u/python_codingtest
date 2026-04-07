import math

m = int(input())
n = int(input())

def is_prime(k):
    if k < 2:
        return False
    if k == 2:
        return True
    if k % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False

    return True

answer = []
for num in range(m, n + 1):
    if is_prime(num):
        answer.append(num)

if not answer:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))