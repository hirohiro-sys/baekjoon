N = int(input())

li = []
for _ in range(N):
    a,b = map(int,input().split())
    li.append((a,b))

# lambda이용해서 오른 수로 정렬 
sorted_li = sorted(li,key=lambda x:(x[1],x[0]))

for i in sorted_li:
    print(*i)
