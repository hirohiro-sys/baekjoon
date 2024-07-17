from collections import deque

# 左右どちらかに方向転換させる関数
def direction_change(d,c):
    if c=="L":
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

# ボード
N = int(input())
board = [[0] * N for _ in range(N)]
# りんごの位置
K = int(input())
for _ in range(K):
    a,b = map(int,input().split())
    board[a-1][b-1] = 1
# X秒後にCの方向に転換
L = int(input())
times = {}
for _ in range(L):
    X,C = input().split()
    times[int(X)] = C

# 上下左右への移動するための配列
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 現在の移動方向を表す変数
direction = 1
# 時間を測る変数
time = 1
# 蛇の初期位置
x,y = 0,0
# 最初に挿入される尻尾の箇所を削除するためキューを使う
snake = deque([[x,y]])
# 蛇のいる場所には2を入れる
board[x][y] = 2

# ここからメイン処理
while True:
    # 次のマスに移動(初期は右に移動)
    x,y = x + dx[direction],y+dy[direction]
    # もし壁にぶつかっていない & 自分にもぶつかっていなかったら
    if 0<=x<N and 0<=y<N and board[x][y]!=2:
        # もし移動したマスにリンゴがなかったら
        if not board[x][y]==1:
            # 尻尾の箇所をなくす
            delX,delY = snake.popleft()
            board[delX][delY] = 0
        # 移動先のマスに蛇がいることを登録してキューにも追加
        board[x][y] = 2
        snake.append([x,y])
        if time in times.keys():
            direction = direction_change(direction,times[time])
        time += 1
    # 壁にぶつかってる or 自分にぶつかっていたら終了して出力
    else:
        exit(print(time))

# https://www.acmicpc.net/problem/3190
