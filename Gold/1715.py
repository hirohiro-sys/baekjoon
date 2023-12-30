import heapq
N = int(input())
cards = list(int(input()) for _ in range(N))
heapq.heapify(cards)
ans = 0
while len(cards)!=1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    sum = A + B
    ans += sum
    heapq.heappush(cards,sum)
print(ans)

"""
https://www.acmicpc.net/problem/1715
"""
