n = int(input())

dp = [0]*91
dp[1] = 1
dp[2] = 1
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])

#問題文は難しそうだけど漸化式はただのフィボナッチ

"""
https://www.acmicpc.net/problem/2193
"""
