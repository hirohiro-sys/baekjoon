li = list(map(int,input().split()))
mn = min(li)
while 1:
    count = 0
    for i in li:
        if mn%i==0:
            count += 1
    if count>2:
        break
    mn += 1
print(mn)

"""
https://www.acmicpc.net/problem/1145
"""
