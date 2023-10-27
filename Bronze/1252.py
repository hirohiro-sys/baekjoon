a,b = input().split()

#2進数を10進数に
a = int(a,2)
b = int(b,2)
ans = a + b

#binで10進数を2進数に 
print(bin(ans)[2:])
