# 入力
N = int(input())
A = list(map(int,input().split()))

# DPのメイン処理
dp = [1] * N
dp2 = [1] * N
for i in range(N-1):
    if A[i]<=A[i+1]:
        dp[i+1] += dp[i]
for i in range(N-1):
    if A[i]>=A[i+1]:
        dp2[i+1] += dp2[i]

# 出力
print(max(max(dp),max(dp2)))

"""
一度解いた値を再利用するため動的計画法を使用
大きな問題を小さい問題に分割して再帰的に解を求めるためDPのトップダウン方式
https://www.acmicpc.net/problem/2491
"""
