N = int(input())
ans = 0
K = 1

while N!=0:
    if N<K:
        K = 1
    N -= K
    K += 1
    ans += 1

print(ans)

"""
問題よく読んでそのまま実装する
数学的思考
"""
