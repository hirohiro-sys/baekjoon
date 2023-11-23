n = int(input())

a = [0] * (n+1)
#1は回数が確定しているため2からスタート
for i in range(2,n+1):
    #各+1は計算回数をカウントしている
    a[i] = a[i-1] + 1
    if i%2==0:
        a[i] = min(a[i],a[i//2]+1)
    if i%3==0:
        a[i] = min(a[i],a[i//3]+1)
　　　　      
print(a[n])
