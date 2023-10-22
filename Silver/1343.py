# 이 코드로 데이터입력을 더 빠르게 할 수 있음
import sys
input = sys.stdin.readline

# 심플하게 생각하면 됨
def ans(S):
    S = S.replace("XXXX","AAAA")
    S = S.replace("XX","BB")

    if S.count("X")!=0:
        return -1
    else:
        return S
    
if __name__=="__main__":
    S = input()
    print(ans(S))
