indices = []
for i in range(5):
    s = input()
    if "FBI" in s:
        indices.append(str(i+1))

if indices:
    print(" ".join(indices))
else:
    print("HE GOT AWAY!")

"""
https://www.acmicpc.net/problem/2857
"""
