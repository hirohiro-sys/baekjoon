n = int(input())
a = list(map(int,input().split()))
# 育つまでに時間がかかる木を早く植えることで最短日数がわかる
a.sort(reverse=True)
ans = []
for i in range(n):
    '''해석
    나무를 심는데 하루 : + 1
    나무가 자라는 시간 : + a[i]
    몇 번째 나무를 심는지 :  + i
    며칠에 초대할 수 있는지 : max(ans) + 1
    '''
    ans.append(1+a[i]+i)
print(max(ans)+1)

# https://www.acmicpc.net/problem/9237
