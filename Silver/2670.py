dp = [float(input()) for _ in range(int(input()))]
for i in range(1,len(dp)): dp[i] = max(dp[i],dp[i]*dp[i-1])
print("%0.3f" % max(dp))
"""
どうやったらその時点の部分最大積を求めれるか考える。出力の際は単位に注意
https://www.acmicpc.net/problem/2670
"""
