from collections import deque

n = input()

stack = deque()

for num in n:
    num = int(num)

    if not stack:
        stack.append(num)
    else:
        pop = stack.pop()

        if pop == 0:
            k = pop + num
        else:
            k = pop * num
        stack.append(k)

print(stack[-1])

