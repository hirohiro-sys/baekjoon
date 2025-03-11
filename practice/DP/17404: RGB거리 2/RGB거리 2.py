n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

ans = float("inf")
for i in range(3):
    dp = [[1000]*3 for _ in range(n)]
    dp[0][i] = a[0][i]
    for j in range(1,n):
        dp[j][0] = min(dp[j-1][1],dp[j-1][2]) + a[j][0]
        dp[j][1] = min(dp[j-1][0],dp[j-1][2]) + a[j][1]
        dp[j][2] = min(dp[j-1][0],dp[j-1][1]) + a[j][2]
    dp[-1][i] = float("inf")
    ans = min(ans,min(dp[-1]))
    
print(ans)
