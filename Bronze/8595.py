import re

n = int(input())
s = input()
ans = list(map(int, re.findall(r'\d+', s)))
print(sum(ans))

"""
https://www.acmicpc.net/problem/8595
"""
