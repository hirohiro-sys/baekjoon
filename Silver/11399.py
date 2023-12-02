n = int(input())
a = list(map(int,input().split()))
a.sort()
#print(a)
ans = [a[0]]
for i in range(1,n):
    ans.append(ans[i-1]+a[i])
print(sum(ans))
