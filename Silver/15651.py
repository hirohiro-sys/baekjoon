n,m = map(int,input().split())
ans = []
def backTraking(depth):
    if depth==m:
        print(*ans)
        return 
    for i in range(1,n+1):
        ans.append(i)
        backTraking(depth+1)
        ans.pop()
backTraking(0)

"""再帰を使わずに簡潔に書く方法
from itertools import product
n, m = map(int,input().split())
answer = []
for combination in product(range(1, n+1), repeat=m):
    print(*combination)
"""
