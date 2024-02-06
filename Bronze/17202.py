A,B = input(),input()
ans = ""
for i in range(len(A)):
    ans += A[i]+B[i]
tmp = []
while len(ans)!=2: 
    for i in range(len(ans)-1): tmp.append(str((int(ans[i])+int(ans[i+1]))%10))
    ans = "".join(tmp)
    tmp = []
print(ans)

"""
https://www.acmicpc.net/problem/17202
"""
