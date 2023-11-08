li = input().split("-")
ans = 0
for i in li[0].split("+"):
    ans += int(i)
    
for i in li[1:]:
    for j in i.split("+"):
        ans -= int(j)
print(ans)
