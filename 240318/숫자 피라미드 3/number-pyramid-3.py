# 변수 선언, 입력
n = int(input())

# 출력
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * j, end = " ")

    print()