# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 출력
if a < b:
    if b < c:
        print(b)
    elif b > c:
        print(c)
    else:
        print(a)
else:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)