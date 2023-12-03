#긴문자열안을 짧은문자열로 탐색하고 차이비교하면됨
a,b = input().split()
min_value_result = 50
for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j]!=b[i+j]:
            count += 1
    min_value_result = min(min_value_result,count)
print(min_value_result)
