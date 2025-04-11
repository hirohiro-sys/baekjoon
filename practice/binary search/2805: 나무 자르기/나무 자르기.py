N,H = map(int,input().split())
A = list(map(int,input().split()))

start,end = 1,max(A)
while start<=end:
    # 切断機の長さ 
    mid = (start+end)//2
    log = 0
    for i in A:
        if i>mid:
            log += i-mid
    # もしすでに目標を上回っていたら切断機をさらに上に指定できる
    if log>=H:
        start = mid + 1
    # たりてなかったら切断機を短くして取れる木の量を増やす
    else:
        end = mid - 1
       
print(end)


"""
https://www.acmicpc.net/problem/2805
"""
