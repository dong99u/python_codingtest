import sys

input = sys.stdin.readline

N = int(input()) # 3

scores = list(map(int, input().rstrip().split())) # [40, 80, 60]

max_score = max(scores)

adjusted_scores = []

for score in scores:
    adjusted_scores.append((score / max_score) * 100)

print(sum(adjusted_scores) / N)

