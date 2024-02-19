# 변수 선언, 입력
arr = input().split()
b = int(arr[0])
a = int(arr[1])

# 출력
for i in range(b, a - 1, -2):
    print(i , end = ' ')