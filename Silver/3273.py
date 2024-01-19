n = int(input())
a = list(map(int,input().split()))
x = int(input())
ans = 0
a.sort()

l,r = 0,n-1
while l<r:
    sm = a[l]+a[r]
    if sm==x:
        ans += 1
        l += 1
        r -= 1
    elif sm < x: l += 1
    else:        r -= 1

print(ans)

"""
https://www.acmicpc.net/problem/3273
"""
