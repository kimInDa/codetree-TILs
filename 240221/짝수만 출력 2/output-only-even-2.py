# 변수 선언, 입력
arr = input().split()
b = int(arr[0])
a = int(arr[1])

# 출력
while b >= a:
    print(b, end = ' ')
    b -= 2