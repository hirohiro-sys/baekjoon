# 素数を判定するテンプレ
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 入力
N = int(input())
A = list(map(int,input().split()))

# 出力
count = 0
for i in A:
    if is_prime(i):
        count += 1
print(count)
