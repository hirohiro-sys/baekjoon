n = int(input())
a = [input() for _ in range(n)]

width,height = 0, 0
for i in range(n): 
    space_width,space_height = 0, 0
    for j in range(n):
        if a[i][j]==".":       space_width += 1
        else:                  space_width = 0
        if a[j][i]==".":       space_height += 1
        else:                  space_height = 0
        if space_width==2:     width += 1
        if space_height==2:    height += 1

print(width,height)
