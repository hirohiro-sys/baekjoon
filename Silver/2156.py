n = int(input())
dp = [0] * 10001
a = [0] * 10001
for i in range(1,n+1):
    a[i] = int(input())

dp[1]=a[1]
dp[2]=a[1]+a[2]
for i in range(3,n+1):
    """
    ・2杯だけ飲む場合
    ・2杯飲んで一つ飛ばして1杯飲む場合
    ・1杯飲んで一つ飛ばして2杯飲む場合
    """
    dp[i] = max(dp[i-1],dp[i-2]+a[i],dp[i-3]+a[i-1]+a[i])
print(dp[n])


"""
https://www.acmicpc.net/problem/2156
"""
