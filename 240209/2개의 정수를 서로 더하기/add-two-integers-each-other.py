# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# 변화
a += b
b += a

# 출력
print(a, b)