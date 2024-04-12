n = int(input())
dp = [0] * 81
dp[1] = 4
dp[2] = 6
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
# 問題文読んで普通のフィボナッチに気付けるか

"""
https://www.acmicpc.net/problem/13301
"""
