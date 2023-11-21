n = int(input())
ans = []

for _ in range(n):
    command = list(input().split())
    if command[1]=="enter":
        ans.append(command[0])
    else:
        ans.pop(ans.index(command[0]))

ans.sort(reverse=True)
for i in ans:
    print(i)
