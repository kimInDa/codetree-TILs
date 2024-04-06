# 변수 선언, 입력
n = int(input())

# 격자 모양 사각형 별 출력
for i in range(2 * n + 1):
    for j in range(2 * n + 1):
        if i % 2 == 0:
            print("* ", end = "")
        else:
            if j % 2 == 0:
                print("*", end = " ")
            else:
                print(" ", end = " ")
    print()