# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
prod = 1

# 1부터 b까지의 수 중 a배수의 곱 구하기
for i in range(1, b + 1):
    if i % a == 0:
        prod *= i

# 출력
print(prod)