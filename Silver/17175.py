n = int(input())
dp = [0] * (n+1)
if n<2: print(1)
else:
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]+1
    print(dp[n]%1000000007)


"""
https://www.acmicpc.net/problem/17175
"""

# フィボナッチの関数呼び出し回数はdp[i-1]とdp[i-2]の2回に加えて自分自身も呼び出すため+1する
