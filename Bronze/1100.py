li = [input() for _ in range(8)]

count = 0
for i in range(8):
    for j in range(8):
        if i%2==0 and j%2==0 and li[i][j]=="F":
            count += 1
        elif i%2!=0 and j%2!=0 and li[i][j]=="F":
            count += 1
    
print(count)

"""
なんの条件を満たすとcount+=1になるかを整理すれば簡単
"""
