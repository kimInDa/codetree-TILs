# 변수 선언, 입력
n = int(input())

# (1, 1)에서 (n, n)까지 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"({i}, {j})", end = " ")

        # (i, j)에서 i + j가 4의 배수가 되는 순간 다음 줄로 넘어감
        if (i + j) % 4 == 0:
            print()