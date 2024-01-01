a,b = map(int,input().split())
ans = 0
for i in range(1,a+1):
    if str(b) in str(i):
        ans += str(i).count(str(b))
print(ans)

"""
https://www.acmicpc.net/problem/14912
"""
