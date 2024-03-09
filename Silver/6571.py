dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3,1001):
  dp[i] = dp[i - 1] + dp[i - 2]

while 1:
  a,b = map(int,input().split())
  if a==0 and b==0: break
  ans = 0
  for i in range(1,1001):
    if a <= dp[i] <= b:
      ans+=1
  print(ans)


"""
https://www.acmicpc.net/problem/6571
"""

# bは10**100だからピボナッチの1000番目の数が101桁以上ならよし
