# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# 출력
if a < b:
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b:
    print(1)
else:
    print(0)