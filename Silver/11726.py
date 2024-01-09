n = int(input())
# 変にindexError起こさないためにも初めから制約の大きさにする
dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]
print(dp[n]%10007)

"""
https://www.acmicpc.net/problem/11726
"""
