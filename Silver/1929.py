def isprime(n: int) -> bool:

    # 1以下は素数ではないので排除
    if n <= 1:
        return False

    # 2からnの2分の1乗までのループ
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            # 割り切れる値があれば素数ではないのでFalseを返す
            return False
    # ここまでくれば素数
    return True

m,n = map(int,input().split())
for i in range(m,n+1):
  if isprime(i):
    print(i)

"""
素数判定アルゴリズムは自分で描けるようにしておく
"""
