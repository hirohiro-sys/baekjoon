grade,score = 0,0
for i in range(20): 
    s = input().split()
    # もっと別のいい書き方あるはず....
    if s[-1]=="A+": score += float(s[-2])*4.5; grade+=float(s[-2])
    elif s[-1]=="A0": score += float(s[-2])*4.0; grade+=float(s[-2])
    elif s[-1]=="B+": score += float(s[-2])*3.5; grade+=float(s[-2])
    elif s[-1]=="B0": score += float(s[-2])*3.0; grade+=float(s[-2])
    elif s[-1]=="C+": score += float(s[-2])*2.5; grade+=float(s[-2])
    elif s[-1]=="C0": score += float(s[-2])*2.0; grade+=float(s[-2])
    elif s[-1]=="D+": score += float(s[-2])*1.5; grade+=float(s[-2])
    elif s[-1]=="D0": score += float(s[-2])*1.0; grade+=float(s[-2])
    elif s[-1]=="F": score += float(s[-2])*0.0; grade+=float(s[-2])
    else: continue
print(score/grade)

"""他の人のコード
cnt = 0
total = 0.0
arr = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for x in range(20):
    a, b, c = map(str, input().split())
    if c == "P":
        pass
    else:
        cnt = cnt + float(b)
        total = total + float(b)*arr[c]

print(total/cnt)
"""

"""
https://www.acmicpc.net/problem/25206
"""
