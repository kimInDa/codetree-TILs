# 변수 선언, 입력
n = int(input())
satisfied = True

# n이 소수인지 판별
for i in range(2, 1001):
    # 자기 자신 외에 나누어 떨어지는 수가 있으면 소수가 아님
    if n != i and n % i == 0:
        satisfied = False

# 소수이면 "P", 아니면 "C" 출력
if satisfied == True:
    print("P")
else:
    print("C")