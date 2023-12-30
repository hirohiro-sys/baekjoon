import heapq
import sys
n = int(input())
heap = []
for _ in range(n):
    # 入力はやめないとTLEなる
    num = int(sys.stdin.readline())
    if num!=0:
        # pythonのheapqは最小ヒープがベースだから-numで絶対値が大きいものをルートに来るように
        heapq.heappush(heap, (-num))
    else:
        try:
            # さっき-numしたから-1をかけることで1番大きい値を取り出せる
            print(-1*heapq.heappop(heap))
        except:
            print(0)


"""
https://www.acmicpc.net/problem/11279
"""
