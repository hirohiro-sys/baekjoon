n,m = map(int,input().split())
a = list(map(int,input().split()))
l = [None] * m
r = [None] * m
for i in range(m):
    l[i],r[i] = map(int,input().split())

new_a = [None] * (n+1)
new_a[0] = 0
for i in range(n):
    new_a[i+1] = new_a[i] + a[i]

for i in range(m):
    print(new_a[r[i]]-new_a[l[i]-1])
    
"""
累積和の基本問題
"""
