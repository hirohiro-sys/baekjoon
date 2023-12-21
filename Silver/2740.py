n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
m,k = map(int,input().split())
a2 = [list(map(int,input().split())) for _ in range(m)]

ans = [[0 for _ in range(k)] for _ in range(n)]
for N in range(n):
    for K in range(k):
        for M in range(m): 
            ans[N][K] += a[N][M]*a2[M][K]
for i in ans:
    for j in i:
        print(j,end=" ")
    print()


# 파이썬 행렬 곱셈은 N*M 행렬과 M*K 행렬이 만나 N*K행렬을 만든 다는 것만 기억하면 된다.
# https://www.acmicpc.net/problem/2740
