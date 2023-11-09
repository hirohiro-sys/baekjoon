from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
li = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
li2 = list(map(int,stdin.readline().split()))

count = Counter(li)
for i in range(len(li2)):
    # 辞書の性質を抑える
    if li2[i] in count:
        print(count[li2[i]],end=" ")
    else:
        print(0,end=" ")
