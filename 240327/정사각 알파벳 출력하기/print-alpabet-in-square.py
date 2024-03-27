# 변수 선언, 입력
n = int(input())
cnt = 65

# n x n 크기의 알파벳 정사각형 출력
for i in range(n):
    for j in range(n):
        print(chr(cnt), end = "")
        ++cnt

    print()