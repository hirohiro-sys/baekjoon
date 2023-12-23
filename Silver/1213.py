from collections import Counter

s = list(map(str,input()))
s.sort()
count = Counter(s)
odd_count = 0
odd = ""
ans = ""

for i in count:
    if count[i]%2!=0:
        odd_count += 1
        odd += i
    for _ in range(count[i]//2):
        ans += i


if odd_count>1:
    print("I'm Sorry Hansoo")
elif odd_count == 0:
    print(ans + ans[::-1])
else:
    print(ans + odd + ans[::-1])
