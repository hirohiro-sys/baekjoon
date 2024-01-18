# 入力
N,T = map(int,input().split())
li = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(T):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
# print(li)

# 深さ優先探索
def dfs(V):
    visited[V]=1
    for i in li[V]:
        if visited[i]==0:
            dfs(i)

# 出力
ans = 0
for i in range(1,N+1):
    if visited[i]==0:
        # 行けるとこまで行って帰ってきたら+1
        dfs(i)
        ans+=1
print(ans)

"""
https://www.acmicpc.net/problem/11724
"""
