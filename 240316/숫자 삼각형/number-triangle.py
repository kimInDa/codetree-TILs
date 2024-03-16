# 변수 선언, 입력
n = int(input())

# 숫자 삼각형 출력
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end = " ")

    print()