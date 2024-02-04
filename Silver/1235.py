# 入力
n = int(input())
s = [input() for _ in range(n)]

for i in range(1,len(s[0])+1):
    a = []
    for j in range(n):
        if s[j][-i:] in a:
            break
        else:
            a.append(s[j][-i:])
    # もし各文字列の部分文字列が全て違った場合出力
    if len(a)==n:
        print(i)
        break


"""
https://www.acmicpc.net/problem/1235
"""
