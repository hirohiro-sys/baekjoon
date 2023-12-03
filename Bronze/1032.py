n = int(input())
a = [input() for _ in range(n)]

ans = ""
for i in range(len(a[0])):
    tmp = []
    for j in range(n):
        tmp.append(a[j][i])
    if len(set(tmp))==1:
        ans += a[j][i]
    else:
        ans += "?"

ans = "".join(ans)
print(ans)
