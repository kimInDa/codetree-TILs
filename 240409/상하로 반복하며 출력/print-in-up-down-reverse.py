# 변수 선언, 입력
n = int(input())

# 출력
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(i + 1, end = "")
        else:
            print(n - i, end = "")

    print()