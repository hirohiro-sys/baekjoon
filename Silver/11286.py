import heapq
import sys
N = int(input())
heap = []
for _ in range(N):
    # 入力速度上げないと計算量オーバーになる
    X = int(sys.stdin.readline())
    if X!=0:
        # 絶対値の小さい順にpushする時はタプルで
        heapq.heappush(heap,(abs(X),X))
    else:
        if heap: print(heapq.heappop(heap)[1])
        else: print(0)


"""
https://www.acmicpc.net/problem/11286
"""
