import math
n,k = map(int,input().split())
ans = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
print(ans%10007)

#mathライブラリのcombでもっと簡単に組み合わせを求めれる
