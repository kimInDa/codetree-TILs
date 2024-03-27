# 변수 선언, 입력
n = int(input())

# n x n 크기의 알파벳 정사각형 출력
for i in range(n):
    for j in range(65, 65 + n):
        print(chr(j), end = "")

    print()