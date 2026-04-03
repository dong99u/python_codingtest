'''
사전순 정렬하면, 가장 긴 공통 접두사를 가진 쌍은 반드시 정렬 후 인접 위치에 온다.
따라서 2단계로 풀 수 있다:

1단계 - 최대 접두사 길이 L 구하기:
    정렬 후 인접 쌍만 비교하면 L을 구할 수 있다.

2단계 - 원래 입력 순서에서 정답 쌍 찾기:
    L을 알면, 원래 순서대로 각 단어의 앞 L글자를 키로 그룹핑한다.
    각 그룹에서 처음 만나는 두 단어가 해당 그룹의 최선 쌍이다.
    모든 그룹의 최선 쌍 중, S의 입력 순서가 가장 빠른 것이 정답.
    S가 같으면 T의 입력 순서가 가장 빠른 것이 정답.

'''

import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

# 1단계: 정렬 후 인접 비교로 최대 접두사 길이 L 구하기
sorted_words = sorted(words)
max_len = 0

for i in range(1, n):
    a, b = sorted_words[i - 1], sorted_words[i]
    common = 0
    for j in range(min(len(a), len(b))):
        if a[j] == b[j]:
            common += 1
        else:
            break
    max_len = max(max_len, common)

# 2단계: 원래 순서로 순회하며, 접두사(길이 L) 기준으로 그룹핑
# prefix_first: 해당 접두사를 가진 단어 중 가장 먼저 나온 것을 기록
prefix_first = {}        # prefix문자열 → (원래인덱스, 단어)
best = (n, n)            # (S의 인덱스, T의 인덱스) — 작을수록 좋음
ans_s = ans_t = ''

for i, word in enumerate(words):
    if len(word) < max_len:
        continue
    prefix = word[:max_len]

    if prefix not in prefix_first:
        # 이 접두사를 처음 보는 경우: 첫 번째 단어로 기록
        prefix_first[prefix] = (i, word)
    else:
        # 같은 접두사를 가진 단어를 또 만남 → 쌍이 형성됨
        first_i, first_word = prefix_first[prefix]
        if (first_i, i) < best:
            best = (first_i, i)
            ans_s, ans_t = first_word, word

print(ans_s)
print(ans_t)