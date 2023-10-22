A,B,N = map(int,input().split())
for _ in range(N):
    A = (A%B)*10
    ans = A//B
print(ans)

"""
문자열로 하면 파이썬의 경우 15자리까지만 표시가 되서
수학적 관점에서 풀어야됨
"""
