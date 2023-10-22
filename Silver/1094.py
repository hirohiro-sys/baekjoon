num = int(input())
li = [64,32,16,8,4,2,1]

count = 0
for i in range(len(li)):
    if num >= li[i]:
        count += 1
        num -= li[i]
    
    if num <= 0:
        break

print(count)

"""
問題文通り実装する
"""
