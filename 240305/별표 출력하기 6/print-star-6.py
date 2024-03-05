# 변수 선언, 입력
n = int(input())

# 모래시계 상단 출력
for i in range(n):
    # 공백 출력
    for j in range(i):
        print(" ", end = " ")
    
    # 별 출력
    for j in range((2 * n) - (2 * i) - 1):
        print("*", end = " ")

    print()

# 모래시계 하단 출력
for i in range(n - 1):
    # 공백 출력
    for j in range(n - i - 2):
        print(" ", end = " ")

    # 별 출력
    for j in range(3 + (2 * i)):
        print("*", end = " ")
    
    print()