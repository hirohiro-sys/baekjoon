N,M = map(int,input().split())
collection = {}
for i in range(1,N+1):
    S_N = input()
    collection[i],collection[S_N] = S_N,i
for i in range(M):
    S_M = input()
    if S_M.isdigit(): print(collection[int(S_M)])
    else: print(collection[S_M])


"""
https://www.acmicpc.net/problem/1620
"""
