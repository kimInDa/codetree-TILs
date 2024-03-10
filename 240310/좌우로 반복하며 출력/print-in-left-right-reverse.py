# 변수 선언, 입력
n = int(input())

# n에 따라 일의 숫자를 좌우로 반복하며 출력
for i in range(1, n + 1):
    # 홀수행일 경우 1부터 n까지 출력
    if i % 2 != 0:
        for j in range(1, n + 1):
            print(j, end = "")
    # 짝수행일 경우 n부터 1까지 출력
    else:
        for j in range(n, 0, -1):
            print(j, end = "")

    # 각 행이 끝날 때마다 줄바꿈
    print()