K,N = map(int,input().split())
A = [int(input()) for _ in range(K)]
s,e = 1,max(A)

while s<=e:
    mid = (s+e)//2
    LAN = 0
    for i in A:
        LAN += i//mid
    if LAN>=N:
        # もし得られた本数が目標本数以上だったら、さらに最大値を求めるためにmid+1して探索
        s = mid + 1
    else:
        # もし得られた本数が目標未満だったら、mid-1を上限にしてその上で最大値を探索
        e = mid - 1
    
print(e)
