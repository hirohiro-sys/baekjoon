B,C,D = map(int,input().split())
burger = list(map(int,input().split()))
side = list(map(int,input().split()))
drink = list(map(int,input().split()))
burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)
ans = 0
mn = min(B,C,D)
for i in range(mn):
    ans += (burger[i]+side[i]+drink[i])*0.9
ans+=sum(burger[mn::]+side[mn::]+drink[mn::])
print(sum(burger+side+drink))
print(int(ans))

"""
https://www.acmicpc.net/problem/15720
"""
