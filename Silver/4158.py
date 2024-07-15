while True:
    N,M = map(int,input().split())
    if N==0 and M==0:
        break
    # 配列だと要素があるかどうか探すときに重複もあるため計算量かかる
    set_N = set()
    for _ in range(N):
        set_N.add(int(input()))
    ans = 0
    for _ in range(M):
        if int(input()) in set_N:
            ans += 1
    print(ans)

# https://www.acmicpc.net/problem/4158
