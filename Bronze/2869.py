import sys
input = sys.stdin.readline
import math
a,b,v = map(int,input().split())
# 最終的に上がる距離を1日で上がる距離でわると何日で到達できるか求められる
ans = (v-b)/(a-b)
# 繰り上げ 4.2→5
print(math.ceil(ans))
