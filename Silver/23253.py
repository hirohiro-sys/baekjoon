n,m = map(int,input().split())
for _ in range(m):
    true_or_false = True
    x = int(input())
    a = list(map(int,input().split()))
    for i in range(x-1):
        if a[i]<a[i+1]:
            true_or_false = False
            break
    if not true_or_false:
        break

if true_or_false:
    print("Yes")
else:
    print("No")

"""
問題の規則性
https://www.acmicpc.net/problem/23253
"""
