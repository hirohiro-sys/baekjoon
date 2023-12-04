n = int(input())
a = list(map(int,input().split()))
sort_a = sorted(a)
ans = []
for i in range(n):
    ans.append(sort_a.index(a[i]))
    sort_a[ans[-1]] = -1
print(*ans)
