import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_dict = {}
name_dict = {}
for i in range(1, N + 1):
    pocketmon_name = input().rstrip()
    num_dict[i] = pocketmon_name
    name_dict[pocketmon_name] = i


for _ in range(M):
    user_input = input().rstrip()
    if user_input.isalpha():
        print(name_dict[user_input])
    else:
        print(num_dict[int(user_input)])