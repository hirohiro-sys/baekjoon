n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
ans = []
for i in range(n):
    ans.append((i+1) * a[i])
print(max(ans))

"""
https://www.acmicpc.net/submit/2217/70714935
"""
