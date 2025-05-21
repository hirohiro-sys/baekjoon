## 問題リンク
https://www.acmicpc.net/problem/1672

## 解き方
シンプルに問題文をコードに落とし込むだけの問題。Atcoderで言うとBくらい

## コード
```python
n = int(input())
s = list(input())

a = [
    ["A", "C", "A", "G"],
    ["C", "G", "T", "A"],
    ["A", "T", "C", "G"],
    ["G", "A", "G", "T"],
]
char_to_idx = {"A": 0,"G": 1,"C": 2, "T": 3}
while len(s)>1:
    idx2 = char_to_idx[s.pop()]
    idx1 = char_to_idx[s.pop()]
    s.append(a[idx1][idx2])
   
print(s[0])
```
