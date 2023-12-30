K = int(input())
A,B = [1],[0]
for i in range(K):
    A.append(B[i])
    B.append(B[i]+A[i])
print(A[-1],B[-1])

"""
https://www.acmicpc.net/problem/9625
"""
