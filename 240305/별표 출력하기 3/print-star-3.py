# 변수 선언, 입력
n = int(input())

# n 높이의 뒤집어진 정삼각형 출력
for i in range(n):
    # 가운데 정렬을 위한 공백 출력
    for j in range(i):
        print(" ", end = " ")
    
    # 별 출력
    for j in range((2 * n) - (2 * i) - 1):
        print("*", end = " ")
    
    print()