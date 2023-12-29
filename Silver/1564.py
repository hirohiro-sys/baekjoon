N = int(input())
f = 1
for i in range(2,N+1):
    f*=i
    while 1:
        if str(f)[-1]=="0":
            f//=10
        else:
            break
    f %= 1000000
print(str(f)[-5:])

"""
階乗の仕組みがわかれば簡単
https://www.acmicpc.net/problem/1564
"""
