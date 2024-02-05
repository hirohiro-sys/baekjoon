a = [list(map(int,input().split())) for _ in range(9)]
mx = -1
A,B = 0,0
for i in range(9):
    for j in range(9):
        if mx<a[i][j]:
            mx = a[i][j]
            A,B = i+1,j+1
print(mx)
print(A,B)

"""
https://www.acmicpc.net/problem/2566
"""
