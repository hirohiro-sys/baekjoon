s = [input() for _ in range(5)]
mx_len = max(len(i) for i in s)
# print(mx_len)
ans = ""
for i in range(mx_len):
    for j in range(5):
        if i<len(s[j]):
            ans += s[j][i]
print(ans)

"""
https://www.acmicpc.net/problem/10798
"""
