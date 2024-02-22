# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# 출력
if a > 0:
    for i in range(1, b + 1):
        print(a, end = '')