# 변수 선언, 입력
n = int(input())

# 1부터 n까지의 수에 대해, i번째 줄에 i개의 i를 출력(1<= i <= n)
for i in range(n):
    for _ in range(i + 1):
        print(i + 1, end = " ")

    print()