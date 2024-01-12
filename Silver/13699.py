n = int(input())
t = [0] * 37
t[0] = 1
t[1] = 1
t[2] = 2
t[3] = 5
for i in range(4,n+1):
    for j in range(i):
        t[i] += t[j]*t[i-1-j]
print(t[n])

"""
https://www.acmicpc.net/problem/13699
"""
