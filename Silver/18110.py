import sys

# 小数点以下が4以下なら繰り下げ、5以上なら繰り上げする関数
def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)

n = int(sys.stdin.readline().strip())
if n:
  level = []
  for _ in range(n):
    level.append(int(sys.stdin.readline().strip()))

  nn = my_round(n*0.15)
  level.sort()
  if nn > 0:
    print(my_round(sum(level[nn:-nn])/len(level[nn:-nn])))
  else:
    print(my_round(sum(level)/len(level)))
# 問題文よりそもそもnが0なら0を出力
else:
  print(0)
