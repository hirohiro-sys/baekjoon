from itertools import combinations_with_replacement
n,m = map(int,input().split())
for i in combinations_with_replacement(map(str,range(1,n+1)),m): print(*i)

"""
順列関連はitertoolsが便利。backTrakingでも解ける
"""
