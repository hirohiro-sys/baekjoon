n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    del a[0]
    # print(a)
    a.sort()
    diff = []
    for j in range(len(a)-1):
        diff.append(a[j+1]-a[j])
    
    print(f"Class {i+1}")
    print(f"Max {a[-1]}, Min {a[0]}, Largest gap {max(diff)}")

"""
https://www.acmicpc.net/problem/5800
"""
