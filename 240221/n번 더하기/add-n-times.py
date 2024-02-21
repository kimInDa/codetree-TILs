# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
n = int(arr[1])

result = a

# 출력
for _ in range(n):
    result += n
    print(result)