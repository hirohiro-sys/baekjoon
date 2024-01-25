dp = [ [1 for _ in range(i)] for i in range(1,31)]
# print(dp)
for i in range(2,30):    #最初と最後は1のため
    for j in range(1,i): #最初と最後以外の値を求めるため
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # 問題文にある規則通り

n,k = map(int,input().split())
print(dp[n-1][k-1])

"""
https://www.acmicpc.net/problem/16395
"""
