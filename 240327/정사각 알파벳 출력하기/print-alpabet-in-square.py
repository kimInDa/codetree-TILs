# 변수 선언, 입력
n = int(input())
cnt = 'A'

# n x n 크기의 알파벳 정사각형 출력
for _ in range(n):
    for _ in range(n):
        print(cnt, end = "")
        cnt = chr(ord(cnt) + 1)

    print()