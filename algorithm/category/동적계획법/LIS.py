def solution(nums):
    n = len(nums)

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == '__main__':
    print(solution([1, 4, 2, 3, 1, 5, 7, 3]))
    print(solution([3, 2, 1]))