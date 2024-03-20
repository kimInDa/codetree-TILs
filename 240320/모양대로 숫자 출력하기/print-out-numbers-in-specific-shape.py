# 변수 선언, 입력
n = int(input())

# 숫자 출력
for i in range(n):
    for j in range(i):
        print(" ", end = " ")

    for j in range(n - i, 0, -1):
        print(j, end = " ")

    print()