# 基本的な深さ優先探索問題

# 深さ優先探索
def dfs(idx,sum):
    global answer
    if idx>=n:
        return 
    sum += A[idx]
    if s==sum:
        answer += 1
    dfs(idx+1, sum-A[idx])
    dfs(idx+1, sum)

# 入力&実行&出力
n,s = map(int,input().split())
A = list(map(int,input().split()))
answer = 0
dfs(0,0)
print(answer)

"""
https://www.acmicpc.net/problem/1182
"""
