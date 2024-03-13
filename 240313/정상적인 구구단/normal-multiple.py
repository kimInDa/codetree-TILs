# 변수 선언, 입력
n = int(input())

# 구구단 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = { i * j }", end = "")
        if j < n:
            print(",", end = " ")
    print()