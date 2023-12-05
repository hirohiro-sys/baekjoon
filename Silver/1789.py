n = int(input())
sm = 0
ans = 0
for i in range(1,n+1):
    sm += i
    ans += 1
    if sm > n:
        ans -= 1
        break
print(ans)
"普通に全探索"
