s = input()
a = [0] * 10
for i in s:
    if i=="6" or i=="9":
        if a[6]<=a[9]:
            a[6]+=1
        else:
            a[9]+=1
    else:
        a[int(i)]+=1
print(max(a))
