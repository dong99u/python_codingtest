import sys, math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

answer = 0
for num in arr:
    if is_prime(num):
        answer += 1

print(answer)