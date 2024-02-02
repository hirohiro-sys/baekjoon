n = int(input())
dp = [0] * 117
if n<4:
    print(1)
else:
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-3]
    print(dp[n])

"""
https://www.acmicpc.net/problem/14495
"""
