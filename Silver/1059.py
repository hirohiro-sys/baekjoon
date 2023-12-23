L = int(input())
S = list(map(int,input().split()))
n = int(input())
# 二つの区間の間にあるnを探すためソート
S.sort()

if n in S:
    print(0)
else:
    mn = 0
    mx = 0
    for i in S:
        if n>i:
            mn = i
        elif n<i and mx == 0:
            mx = i
    mn += 1
    mx -= 1
    # nより小さいかず + nより大きいかず
    print((n-mn)*(mx+1-n)+(mx-n))

"""
https://www.acmicpc.net/problem/1059
"""
