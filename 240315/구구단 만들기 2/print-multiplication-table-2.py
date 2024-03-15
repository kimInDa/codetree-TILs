# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# 구구단 출력
for i in range(2, 9, +2):
    for j in range(b, a - 1, -1):
        print(f"{j} * {i} = { j * i }", end = " ")
        if j > a:
            print("/", end = " ")
    print()