import functools

def compare(a, b):
    s1 = str(a) + str(b)
    s2 = str(b) + str(a)
    return (int(s1) > int(s2)) - (int(s2) > int(s1))

def solution(numbers):
    sorted_nums = sorted(numbers, key=functools.cmp_to_key(lambda a, b: compare(a, b)), reverse=True)

    answer = ''.join(str(x) for x in sorted_nums)
    return '0' if int(answer) == 0 else answer

if __name__ == '__main__':
    print(solution([6, 10, 2]))