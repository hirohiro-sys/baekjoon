n = int(input())
sm = 0
grade_score = 0
for i in range(n):
    tmp = 0
    s = input().split()
    if s[-1]=="A+": tmp = 4.3
    elif s[-1]=="A0": tmp = 4.0
    elif s[-1]=="A-": tmp = 3.7
    elif s[-1]=="B+": tmp = 3.3
    elif s[-1]=="B0": tmp = 3.0
    elif s[-1]=="B-": tmp = 2.7
    elif s[-1]=="C+": tmp = 2.3
    elif s[-1]=="C0": tmp = 2.0
    elif s[-1]=="C-": tmp = 1.7
    elif s[-1]=="D+": tmp = 1.3
    elif s[-1]=="D0": tmp = 1.0
    elif s[-1]=="D-": tmp = 0.7
    else: tmp = 0.0
    sm += int(s[1])*tmp
    grade_score+=int(s[1])

print("%.2f" % (round(sm/grade_score+10**-10,2)))
