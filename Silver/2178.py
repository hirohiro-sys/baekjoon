from collections import deque
N,M = map(int,input().split())
A = [list(map(int,input())) for _ in range(N)]
#上下左右
d = [(-1,0),(1,0),(0,-1),(0,1)]
q = deque()
q.append((0,0))

def bfs():
    while q:
        # 現在の位置を取得
        x,y = q.popleft()
        for k in range(len(d)):
            # 位置更新
            dx = x + d[k][0]
            dy = y + d[k][1]
            # dx,dyが範囲内で
            if 0<=dx<N and 0<=dy<M:
                # 問題文より通れる位置なら
                if A[dx][dy]==1:
                    # 前回の位置の値に1を足して新しい位置に更新
                    A[dx][dy] = A[x][y] + 1
                    # 次の反復で現在の位置を取得するためにキューに現在地を追加
                    q.append((dx,dy))

bfs()
print(A[N-1][M-1])

"""
https://www.acmicpc.net/problem/2178
"""
