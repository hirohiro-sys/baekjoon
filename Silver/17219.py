from collections import defaultdict
n,m = map(int,input().split())
li_n = [input().split() for _ in range(n)]
li_m = [input() for _ in range(m)]
dic = defaultdict(list)
for key,value in li_n:
    dic[key].append(value)
for i in li_m:
    for j in dic.get(i,[]):
        print(j)
