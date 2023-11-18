# 入出力みて規則を探す
N = input()
N = sorted(N,reverse=True)

if N[-1]!="0":
    print(-1)
else:
    sm = 0
    for i in N:
        sm += int(i)
    if sm%3!=0:
        print(-1)
    else:
        print("".join(N))
