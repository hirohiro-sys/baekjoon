n = int(input())

if n<3:
    dp = [0,1,1]
    print(dp[n])
else:
    dp =  [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2] 
    print(dp[n])

"""
https://www.acmicpc.net/problem/10826
"""
