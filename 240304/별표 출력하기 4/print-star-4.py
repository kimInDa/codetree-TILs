# 변수 선언, 입력
n = int(input())

# 길이가 n인 직각삼각형을 뒤집어 출력
for i in range(n):
    for j in range(n - i):
        print("*", end = " ")
    print()

# 길이가 n인 직각삼각형 출력
for i in range(n - 1):
    for j in range(i + 2):
        print("*", end = " ")
    print()