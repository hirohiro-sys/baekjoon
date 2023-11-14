N = int(input())
S = input()
ans = 0

for i in range(len(S)):
    ans += (ord(S[i])-96)*(31**i)

# ハッシュ値が極端に大きくなることを避けて計算の安定性を保つ。1234567891は一般的に使われる適当な素数。
print(ans%1234567891)
