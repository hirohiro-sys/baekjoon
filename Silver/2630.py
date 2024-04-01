import sys

def cut(x,y,n):
    global white,blue
    color = paper[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if color!=paper[i][j]:
                cut(x,y,n//2) //1面
                cut(x,y+n//2,n//2) //2面
                cut(x+n//2,y,n//2) //3面
                cut(x+n//2,y+n//2,n//2) //4面
                return 
    
    if color==0:
        white += 1
    else:
        blue += 1

if __name__=="__main__":
    n = int(sys.stdin.readline())
    paper = [list(map(int,input().split())) for _ in range(n)]
    white,blue = 0,0
    cut(0,0,n)
    print(white,blue,sep="\n")

"""
https://www.acmicpc.net/problem/2630
"""
