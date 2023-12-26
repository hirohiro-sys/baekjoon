S = input()
stack = []
ans = 0
for i in range(len(S)):
    if S[i]=="(":
        stack.append("(")
    else:
        if S[i-1]=="(":
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)   
"""
規則を見つければ簡単
https://www.acmicpc.net/problem/10799
"""
