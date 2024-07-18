s = list(input())
i = 0
while i<len(s):
    if s[i]=="<":
        i = s.index(">",i)+1
    elif s[i].isalnum():
        start = i
        while i<len(s) and s[i].isalnum():
            i += 1
        s[start:i] = reversed(s[start:i])
    else:
        i += 1
print("".join(s))

# https://www.acmicpc.net/problem/17413
