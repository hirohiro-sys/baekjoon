import sys
input = sys.stdin.readline
n,m,b = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(n)]

ans = 100000000000000000000000000000
height = 0
for i in range(257):
    mn = 0
    mx = 0
    for j in range(n):
        for k in range(m):
            if table[j][k]<i:
                mn += (i-table[j][k])
            else:
                mx += (table[j][k]-i)
                
    inv = mx + b
    if inv<mn:
        continue
    time = 2*mx+mn
    if time<=ans:
        ans = time
        height = i
        
print(ans,height)
