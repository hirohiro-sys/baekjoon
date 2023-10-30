import math
a,b = map(int,input().split())
GCD = math.gcd(a,b)
LCM = (a*b) // GCD
print(GCD,LCM)

"""
最大公約数はGCDで
最小公倍数は値同士でかけた値をGCDで割る
"""
