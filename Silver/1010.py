import math
N = int(input())
for _ in range(N):
    a,b = map(int,input().split())
    # 조합론 공식대로 구현
    ans = math.factorial(b)//(math.factorial(a)*math.factorial(b-a))
    print(ans)
