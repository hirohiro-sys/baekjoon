# ビンゴ判定ロジック
def check():
    curr_bingo = 0
    for i in range(5):
        if bingo[i] == [0] * 5:
            curr_bingo += 1
    for i in range(5):
        if all(bingo[j][i] == 0 for j in range(5)):
            curr_bingo += 1
    if all(bingo[i][i] == 0 for i in range(5)):
        curr_bingo += 1
    if all(bingo[i][4 - i] == 0 for i in range(5)):
        curr_bingo += 1
    return curr_bingo

# ビンゴシートと呼ばれる数字を受け取る
bingo = [list(map(int, input().split())) for _ in range(5)]
speak = []
for _ in range(5):
    speak += list(map(int, input().split()))

count = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if speak[i] == bingo[x][y]:
                bingo[x][y] = 0
                count += 1

    if count >= 12:
        ans = check()
        if ans >= 3:
            print(i + 1)
            break


"""
https://www.acmicpc.net/problem/2578
"""
