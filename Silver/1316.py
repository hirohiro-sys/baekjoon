# 入力
n = int(input())

ans = n
for i in range(n):
    s = input()
    for j in range(0,len(s)-1):
        # もし同じ文字ならスルー
        if s[j]==s[j+1]:
            pass
        # 文字が連続していない & この先同じ文字が来たらグループ単語ではないから−１する
        elif s[j] in s[j+1:]:
            ans -= 1
            break      
print(ans)
