# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
n = int(arr[1])

# 출력
for _ in range(n):
    a += n
    print(a)