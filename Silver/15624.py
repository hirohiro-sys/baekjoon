n = int(input())
dp = [0,1,1]
for i in range(3,n+1):
    dp.append((dp[i-1]+dp[i-2])%1000000007)
print(dp[n])

"""数学的アプローチ
n = int(input())
a,b = 0,1
for _ in range(n):
    a,b = b%1000000007,a+b
print(a)
"""

"""
https://www.acmicpc.net/problem/15624
普通に解くとメモリ超過、数学的に解いても出力の時に1000000007で割るとTLEが出る(大きな数字同士で計算しているため)
"""
