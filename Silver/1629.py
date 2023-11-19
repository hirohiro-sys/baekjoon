def ans(a,b,c):
    # b乗する必要ないためa%c
    if b==1:
        return a%c
    # 2**16 ➡︎ 2**8 * 2**8みたいな感じで分割できる
    elif b%2==0:
        return (ans(a,b//2,c)**2) % c
    """
    奇数の指数の場合、指数を偶数と奇数の部分に分割し、
    偶数の部分を効率的に計算してから奇数の部分にaをかけることで、
    計算を効率的に進められる
    """
    else:
        return ((ans(a,b//2,c)**2)*a) % c
    
a,b,c = map(int,input().split())
print(ans(a,b,c))
