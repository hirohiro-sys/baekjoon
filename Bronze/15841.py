dp = [0] * 501
dp[1] = 1
dp[2] = 1
for i in range(3,501):
    dp[i] = dp[i-1]+dp[i-2]

while 1:
    n = int(input())
    if n==-1:
        break
    print(f"Hour {n}: {dp[n]} cow(s) affected")

"""
問題文を見れば普通にピボナッチ数列だとわかる
https://www.acmicpc.net/problem/15841
"""
