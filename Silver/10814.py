n = int(input())

li = []
for i in range(n):
    a,b = input().split()
    li.append((int(a),b))

sorted_li = sorted(li,key=lambda x:(x[0]))
for i in sorted_li:
    print(*i)
