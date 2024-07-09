# 問題文より100*100の配列準備
A = [[0]*100 for _ in range(100)]

ans = 0
for _ in range(4):
    i,j,x,y = map(int,input().split())
    # 今回は座標の点ではなくボックスを見るのでi~x+1ではない
    for a in range(i,x):
        for b in range(j,y):
            if A[a][b]==0:
                A[a][b]=1
                ans += 1
               
print(ans)            

# https://www.acmicpc.net/problem/2669
