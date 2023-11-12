N,K = map(int,input().split())
A = [int(input()) for _ in range(N)]

A.sort(reverse=True)
ans = 0
for i in A:
    ans += K//i
    K %= i
    
print(ans)
