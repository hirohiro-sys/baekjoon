N = int(input())
A = list(map(int,input().split()))
mx,ans = 0, 0
for i in range(N-1,-1,-1):
    mx = max(mx,A[i])
    ans = max(ans,mx-A[i])
print(ans)

"""
https://www.acmicpc.net/problem/25644
"""
