N = int(input())
A = list(map(int,input().split()))
A2 = sorted(set(A))
li = {v:i for i,v in enumerate(A2)}
for i in A:
    print(li[i],end=" ")
