n = int(input())
dp = [0]*1000001
dp[1] = 1
dp[2] = 2
if n<3:
    print(n)
else:
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    print(dp[n])


"""
https://www.acmicpc.net/problem/1904
"""

# シルバーくらいのDPだと問題文をヒントに漸化式を探れば意外と簡単
