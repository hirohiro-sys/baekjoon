from collections import deque

def BFS(v):
    queue = deque([v])
    while queue:
        q = queue.popleft()
        if q==K:
            return A[q]
        for next in (q-1,q+1,2*q):
            if 0<=next<MAX and not A[next]:
                A[next] = A[q] + 1
                queue.append(next)

MAX = 100001
N,K = map(int,input().split())
A = [0] * MAX
print(BFS(N))

"""
https://www.acmicpc.net/problem/1697
"""
