n = [int(input()) for _ in range(8)]
sm = 0
ans = []
sorted_n = sorted(n,reverse=True)
for i in range(8):
    if n[i] in sorted_n[:5]:
        sm += n[i]
        ans.append(i+1)
print(sm)
print(*ans)

"""
https://www.acmicpc.net/problem/2822
"""
