# 변수 선언, 입력
n = int(input())

# 마름모 상단 출력
for i in range(n):
    # 공백 출력
    for j in range(n - (i + 1)):
        print(" ", end = "")
    
    # 별 출력
    for j in range((2 * i) + 1):
        print("*", end = "")
    
    print()


# 마름모 하단 출력
for i in range(n - 1):
    # 공백 출력
    for j in range(i + 1):
        print(" ", end = "")

    # 별 출력
    for j in range((2 * n) - (2 * i) - 3):
        print("*", end = "")
    
    print()