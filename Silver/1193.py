# 입력
N = int(input())
line = 1

# 해당 수가 무슨 줄에 있는지 찾음
while N>line:
    N-=line
    line+=1

# 짝수 줄에 있는 경우
if line%2==0:
    a = N
    b = line-N+1
# 홀수 줄에 있는 경우
else:
    a = line - N + 1
    b = N

# 출력
print(f"{a}/{b}")

"""
문제 규칙을 알아야 풀 수 있는 수학문제
"""
