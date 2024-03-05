# 변수 선언, 입력
n = int(input())

# 높이가 n인 정삼각형 출력
for i in range(n):
    # 가운데 정렬을 위한 공백 출력
    for j in range(n - 1 - i):
        print(" ", end = " ")
    
    # 별표 출력
    for j in range(2 * i + 1):
        print("*", end = " ")
    
    print()