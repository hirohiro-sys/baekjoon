t = int(input())
dp = [0] * 69

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,69):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
# print(dp)
for i in range(t):
    n = int(input())
    print(dp[n])

"""
https://www.acmicpc.net/problem/9507
"""
