# 변수 선언, 입력
n = int(input())
cnt = 1

# n * n 숫자 사각형 출력
for i in range(1, n + 1):
    if i % 2 == 0:
        for j in range(cnt + n - 1, cnt -1, -1):
            print(j, end = " ")
            cnt += 1
    else:
        for j in range(cnt, cnt + n):
            print(j, end = " ")
            cnt += 1
    print()