n,m = map(int,input().split())
a = [0] * n
for i in range(m):
    i,j,k = map(int,input().split())
    for idx in range(i,j+1):
        a[idx-1] = k
    # print(a)
for i in a:
    print(i,end=" ") 

"""
https://www.acmicpc.net/problem/10810
"""
