natural_num = set(range(1,10001))
generated_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

# 문제에서 셈프넘은 생성자가 없는 수라서 이런 식이 된다 
self_num = sorted(natural_num-generated_num)

for i in self_num:
    print(i)

"""
문제이해가 힘듬
"""
