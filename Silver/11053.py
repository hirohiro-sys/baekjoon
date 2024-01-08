N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)

ans = 0
dp = [0] * (N+1)
for i in range(1,N+1):
    for j in range(i):
        if A[j]<A[i]:
            dp[i] = max(dp[i],dp[j]+1)
    ans = max(ans, dp[i])

print(ans)

"""
https://www.acmicpc.net/problem/11053
=========================================
11722の問題もリストをreverseすれば同じコードで解ける
"""
