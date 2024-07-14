N,K = map(int,input().split())

a = list(range(1,N+1))
ans = []
cnt_idx = 0
for _ in range(N):
    cnt_idx += K-1
    if cnt_idx>=len(a):
        cnt_idx = cnt_idx%len(a)
    ans.append(str(a.pop(cnt_idx)))
  
print("<",", ".join(ans),">",sep="")

# https://www.acmicpc.net/problem/1158
