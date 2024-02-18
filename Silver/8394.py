n,a,b = int(input()),1,2
for i in range(3, n+1):  a, b = b, (a + b) % 10
print(b)

"""
https://www.acmicpc.net/problem/8394
"""
