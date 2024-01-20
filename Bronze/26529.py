n = int(input())
dp = [0] * 46
dp[0] = 1
dp[1] = 1
for _ in range(n):
    m = int(input())    
    for i in range(2,m+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[m])


"""
https://www.acmicpc.net/problem/26529
"""
