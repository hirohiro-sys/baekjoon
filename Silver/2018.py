n = int(input())
ans = 0
for i in range(1,n+1):
    curr_sm = 0
    j = i
    while curr_sm<n:
        curr_sm += j
        j+=1
    if curr_sm==n:
        ans += 1
print(ans)

"""
しゃくとり法
"""
