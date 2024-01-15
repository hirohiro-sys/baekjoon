T = int(input())
dp = [0] * 10001
dp[1] = 1
dp[2] = 1
for i in range(3,10001):
    dp[i] = dp[i-1] + dp[i - 2]
for i in range(T):
    a,b = map(int,input().split())
    ans = dp[a]%b
    print(f"Case #{i+1}: {ans}")

"""
https://www.acmicpc.net/problem/9711
"""
