N = int(input())
dp = [0,0,1,0,1]
for i in range(5,N+1):
    if dp[i-1]+dp[i-3]+dp[i-4]==3:
        dp.append(0)
    else:
        dp.append(1)
print("SK" if dp[N]==1 else "CY")

"""
https://www.acmicpc.net/problem/9658
"""
# 今回は最後に取った人が負け
