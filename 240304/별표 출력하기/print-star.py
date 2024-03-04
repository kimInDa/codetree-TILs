# 변수 선언, 입력
n = int(input())

# 길이가 n인 직각삼각형 출력
for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
    print()

# 길이가 n-1 인 직각삼각형을 뒤집어 출력
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()