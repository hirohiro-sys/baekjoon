from collections import deque

n,m = map(int,input().split())
a = [list(map(int,input())) for _ in range(n)]

dire = [(-1,0),(1,0),(0,-1),(0,1)]
queue = deque([(0,0)])
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(len(dire)):
            dx = x + dire[i][0]
            dy = y + dire[i][1]
            if 0<=dx<n and 0<=dy<m:
                if a[dx][dy]==1:
                    a[dx][dy] = a[x][y] + 1
                    queue.append((dx,dy))

bfs()
print(a[n-1][m-1])
