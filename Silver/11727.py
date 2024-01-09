N = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3
for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]*2
print(dp[N]%10007)

"""
2*n 타일링問題は実際に通りの増え方を書き出すとわかりやすい
https://www.acmicpc.net/problem/11727
"""
