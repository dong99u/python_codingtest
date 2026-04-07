import sys
from collections import Counter

input = sys.stdin.readline

s_len, p_len = map(int, input().split())
s = input().rstrip()
a, c, g, t = map(int, input().split())

i = 0
j = i + p_len - 1

counter = Counter(s[i:j + 1])

answer = 0

while j < s_len:
    if (counter['A'] >= a and counter['C'] >= c and
            counter['G'] >= g and counter['T'] >= t):
        answer += 1

    j += 1
    if j < s_len:
        counter[s[j]] += 1
        counter[s[i]] -= 1
        i += 1

print(answer)
