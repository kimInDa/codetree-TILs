# 변수 선언, 입력
n = int(input())
satisfied = False

# n이 합성수인지 판별
# 1보다 크면서 소수가 아니면 합성수
for i in range(2, 501):
    if n % i == 0:
        satisfied = True

# 합성수이면 "C", 아니면 "N" 출력
if satisfied == True:
    print("C")
else:
    print("N")