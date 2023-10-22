S = input().upper()
S2 = list(set(S))

li = []
for i in S2:
    ct = S.count(i)
    li.append(ct)

if li.count(max(li)) > 1:
    print("?")
else:
    mx_idx = li.index(max(li))
    print(S2[mx_idx])
