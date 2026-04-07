operator = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

expression = input()

stack = []

answer = []
for exp in expression:
    if exp not in operator: # 숫자라면
        answer.append(exp)
    else: # 연산자라면
        if exp == '(':
            stack.append(exp)
            continue
        if exp == ')':
            while True:
                op = stack.pop()
                if op != '(':
                    answer.append(op)
                else:
                    break
            continue

        if not stack or operator[stack[-1]] < operator[exp]: # 넣는 연산자의 순위가 스택의 top보다 순위가 더 높다면
            stack.append(exp)
        else:
            while stack and operator[stack[-1]] >= operator[exp]:
                answer.append(stack.pop())
            stack.append(exp)

while stack:
    answer.append(stack.pop())

print(''.join(answer))