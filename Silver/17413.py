s = list(input())

i = 0
start = 0
while i < len(s):
    # <>内の処理
    if s[i]=="<":
        while i<len(s) and s[i]!=">":
            i += 1
        i += 1
    # <>外の処理
    elif s[i].isalnum():
        start = i
        while i<len(s) and s[i].isalnum():
            i += 1
        s[start:i] = s[start:i][::-1]
    else: 
        i += 1

print("".join(s))

# https://www.acmicpc.net/problem/17413
