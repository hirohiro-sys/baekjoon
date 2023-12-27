h,w = map(int,input().split())
a = [input() for _ in range(h)]

for i in range(h):
    tmp = False
    cnt = 0    
    for j in range(w):
        if a[i][j]=="c":
            tmp = True
            cnt = 0
            print(0,end=" ")
        else:
            if tmp:
                cnt += 1
                print(cnt,end=" ")
            else:
                print(-1,end=" ")
    print()


"""
https://www.acmicpc.net/problem/10709
"""
