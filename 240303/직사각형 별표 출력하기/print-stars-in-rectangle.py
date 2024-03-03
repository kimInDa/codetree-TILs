# 변수 선언, 입력
arr = input().split()
n = int(arr[0])
m = int(arr[1])

# 직사각형 n * m 별표 출력
for _ in range(n):
    for _ in range(m):
        print("*", end = ' ')
    print()