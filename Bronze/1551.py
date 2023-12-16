# N, K = map(int, input().split())
# arr = list(map(int, input().split(',')))

# for i in range(K):
#     res = []
#     for j in range(N - i - 1):
#         res.append(arr[j + 1] - arr[j])
#     arr = res

# print(",".join(map(str, arr)))


N,K = map(int,input().split())
A = list(map(int,input().split(",")))

for i in range(K):
    tmp = []
    for j in range(N-i-1):
        tmp.append(A[j+1]-A[j])
    A = tmp

print(",".join(map(str,A)))


https://www.acmicpc.net/problem/1551
