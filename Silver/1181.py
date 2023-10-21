# 入力
n = int(input())
# 重複を取り除くためにsetで管理
li = set()
for i in range(n):
    s = input()
    li.add(s)
# lambdaを使って昇順にソート & 長さが同じ場合は辞書順にする
sorted_strings = sorted(li, key=lambda x: (len(x), x))
# 出力
for i in sorted_strings:
    print(i)
