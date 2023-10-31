import math
m = int(input())
n = int(input())
li = []
for i in range(m,n+1):
    if math.sqrt(i)==int(math.sqrt(i)):
        li.append(i)

if li:
    print(sum(li))
    print(li[0])
else:
    print(-1)
