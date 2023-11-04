num = int(input())
li = []
for _ in range(num):
    a,b = map(int,input().split())
    li.append((a,b))

for i in li:
    grade = 1
    for j in li:
        # 自分より値が高いやつが来たら+1して自分の順位を下げる
        if i[0]<j[0] and i[1]<j[1]:
            grade += 1
    print(grade,end=" ")

# 시간복잡도는 O(50**2)
