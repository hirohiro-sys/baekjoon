# 0と1の個数が増える規則性を探せば簡単に解ける
# a,b = b, a+b
T = int(input())
for _ in range(T):
    zero_count,one_count = 1,0
    N = int(input())
    for _ in range(N):
        zero_count,one_count = one_count,zero_count+one_count
    print(zero_count,one_count)


"""
https://www.acmicpc.net/problem/1003
"""
