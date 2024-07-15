N,K = map(int,input().split())
S = input()

cnt = K
stack = []
for num in S:
    while stack and cnt>0 and num>stack[-1]:
        # stackを使わず1つの配列からの値削除の場合、削除にO(n)かかり合計でO(n**2)になってしまう
        stack.pop()
        cnt -= 1
    stack.append(num)

print("".join(stack[:N-K]))

# https://www.acmicpc.net/problem/2812
