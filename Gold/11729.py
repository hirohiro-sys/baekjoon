def hanoi(n,start,to,end):
    # 再帰の脱出点
    if n==1:
        print(start,end)
    else:
        # もし入力が3の場合
        # ここで3回出力
        hanoi(n-1,start,end,to)
        # ここで1回出力
        print(start,end)
        # ここで3回出力
        hanoi(n-1,to,start,end)
        
N = int(input())
# 総移動回数
print(2**N-1)
hanoi(N,1,2,3)

"""
再帰処理の流れをトレースしながら確認する
"""
