# 변수 선언, 입력
n = int(input())

# 두자리 홀수로 이루어진 n * n 크기의 정사각형 출력
for i in range(n):
    for j in range(n):
        print(2 * (i + j + 1) + 9, end = " ")
    
    print()