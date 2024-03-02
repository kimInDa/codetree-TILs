# 변수 선언, 입력
n = int(input())
satisfied = True

# n이 소수인지 판별
for i in range(2, 1001):
    if n != i and n % i == 0:
        satisfied = False

# 소수이면 "P", 아니면 "C" 출력
if satisfied == True:
    print("P")
else:
    print("C")