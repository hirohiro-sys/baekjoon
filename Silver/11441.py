N = int(input())
A = list(map(int,input().split()))
new_A = [0] * (N + 1)
for i in range(N):
    new_A[i+1] = new_A[i] + A[i]
Q = int(input())
for i in range(Q):
    x,y = map(int,input().split())
    print(new_A[y] - new_A[x-1])
