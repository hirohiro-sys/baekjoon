# 入力と下準備
from collections import deque
N,M,V = map(int,input().split())
A = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    A[a][b]=A[b][a]=1
visit = [0] * (N+1)

# DFS(深さ優先探索)
def dfs(V):
    visit[V]=1
    print(V,end=" ")
    for i in range(1,N+1):
        if visit[i]==0 and A[V][i]==1:
            dfs(i)
            
# BFS(幅優先探索)
def bfs(V):
    visit[V]=0
    queue = deque()
    queue.append(V)
    while queue:
        V = queue.popleft()
        print(V,end=" ")
        for i in range(1,N+1):
            if visit[i]==1 and A[V][i]==1:
                queue.append(i)
                visit[i]=0

# 実行
dfs(V)
print()
bfs(V)


"""
https://www.acmicpc.net/problem/1260
"""
