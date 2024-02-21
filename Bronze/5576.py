w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]
w.sort(reverse=True)
k.sort(reverse=True)
print(sum(w[:3]),sum(k[:3]))

"""
https://www.acmicpc.net/problem/5576
"""
