# 入力 & 隣接リスト作成
N = int(input())
T = int(input())
li = [[] for _ in range(N+1)]
for _ in range(T):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
# print(li)

# 深さ優先探索
visited = [0] * (N+1)
def dfs(V):
    visited[V] = 1
    for i in li[V]:
        if visited[i]==0:
            dfs(i)

# 実行 & 出力
dfs(1)
# print(visited)
print(sum(visited)-1)

"""
https://www.acmicpc.net/problem/2606
"""

"""BFS같은 경우
	from collections import deque
visited[1]=1 # 1번 컴퓨터부터 시작이니 방문 표시
Q=deque([1])
while Q:
    c=Q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            Q.append(nx)
            visited[nx]=1
print(sum(visited)-1)
"""
