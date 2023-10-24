n = int(input())

for i in range(n,3,-1):
    count = 0
    for j in str(i):
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="5" or j=="6" or j=="8" or j=="9":
            continue
        else:
            count += 1
            if count==len(str(i)):
                print(i)
                exit()
