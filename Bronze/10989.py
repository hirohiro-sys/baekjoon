import sys
input = sys.stdin.readline

n = int(input())
li = [0] * (10000+1)

for i in range(n):
    li[int(input())] += 1


for i in range(len(li)):
    if li[i]!=0:
        for _ in range(len(li[i])):
            print(i)
