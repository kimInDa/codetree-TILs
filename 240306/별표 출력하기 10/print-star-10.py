# 변수 선언, 입력
n = int(input())

# 행에 따라 다른 별 출력
for i in range(n * 2):
    if i % 2 != 0:
        for j in range(n - (i - 1) // 2):
            print("*", end = " ")
        print()
    else:
        for j in range(1 + (i // 2)):
            print("*", end = " ")
        print()