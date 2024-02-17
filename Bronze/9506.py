def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

while 1:
    n = int(input())
    if n==-1:
        break
    a = find_divisors(n)
    result = sum(a)
    if n!=result:
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = {' + '.join(str(x) for x in a)}")


"""
https://www.acmicpc.net/problem/9506
"""
