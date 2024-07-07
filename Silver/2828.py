n,m = map(int,input().split())

start = 1
end = m
distance = 0
for _ in range(int(input())):
    p = int(input())
    # リンゴがバスケットの左の範囲外に落ちた場合、バスケットを左に移動させてリンゴを収集
    if p < start:
        distance += (start-p)
        start = p
        end = start+m-1
    # リンゴがバスケットの右の範囲外に落ちた場合、バスケットを右に移動させてリンゴを収集
    elif p > end:
        distance += (p-end)
        end = p
        start = end-m+1
        
print(distance)

"""
https://www.acmicpc.net/problem/2828
"""
