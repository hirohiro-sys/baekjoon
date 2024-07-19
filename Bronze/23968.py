N,K = map(int,input().split())
A = list(map(int,input().split()))

# バブルソートは1周するごとに後ろの値を見なくて良くなる
for i in range(N-1,0,-1):
    for j in range(i):
        if A[j]>A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]
            K-=1
        if K==0:
            exit(print(A[j],A[j+1]))
print(-1)

# https://www.acmicpc.net/problem/23968
