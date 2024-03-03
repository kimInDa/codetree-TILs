# 변수 선언, 입력
n = int(input())

# 정사각형 별표 출력
for _ in range(n):
    for _ in range(n):
        print("*", end = '')
    print()