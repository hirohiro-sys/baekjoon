t = int(input())

ans = []
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(2):
        a.append(list(map(int, input().split())))

    if len(a[0]) == 1:
        print(max(a[0][0], a[1][0]))
    else:
        a[0][1] += a[1][0]
        a[1][1] += a[0][0]
        for i in range(2, n):
            a[0][i] += max(a[1][i - 1], a[1][i - 2])
            a[1][i] += max(a[0][i - 1], a[0][i - 2])
        ans.append(max(a[0][-1], a[1][-1]))
        
print(*ans,sep='\n')

"""
ロジックの発想自体は難しくない
https://www.acmicpc.net/problem/9465
"""
