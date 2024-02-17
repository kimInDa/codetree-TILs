# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 출력
if a < b:
    # a < b < c 일때
    if b < c: 
        print(b)
    # c < a < b 일때
    elif a < c: 
        print(a)
    # a < c < b 일때
    else:
        print(c)
# b < a 기준
else:
    # c < b < a 일때
    if b > c:
        print(b)
    # b < a < c 일때
    elif a < c:
        print(a)
    # b < c < a 일때
    else:
        print(c)