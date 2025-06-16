import functools

def compare(a, b):
    str1 = str(a) + str(b)
    str2 = str(b) + str(a)

    return (int(str1) > int(str2)) - (int(str1) < int(str2))

def solution(numbers):
    sorted_nums = sorted(numbers, key=functools.cmp_to_key(lambda a, b: compare(a, b)), reverse=True)

    answer = ''.join(str(x) for x in sorted_nums)

    return '0' if answer == '0' else answer

if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))