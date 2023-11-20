from collections import deque

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    A = deque(list(map(int,input().split())))
    cnt = 1
    while True:
        if M==0:
            if A[0]==max(A):
                print(cnt)
                break
            else:
                A.append(A.popleft())
                M = N - 1
        else:
            if A[0]==max(A):
                A.popleft()
                cnt += 1
                N-=1
                M-=1
            else:
                A.append(A.popleft())
                M-=1       
