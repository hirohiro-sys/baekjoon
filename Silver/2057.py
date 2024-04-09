n = int(input())
# 0と1の階乗
fact = [1,1]
# intで扱えるのは20!まで
for i in range(2,21):
    fact.append(fact[i-1]*i)
# あとは普通に求める
sum = 0
for i in range(20,-1,-1):
    if sum+fact[i]<n:
        sum += fact[i]
    elif sum+fact[i]==n:
        exit(print("YES"))
print("NO")

"""
https://www.acmicpc.net/problem/2057
"""
