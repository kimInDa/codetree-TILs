# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
prod = 1

# a의 b제곱 구하기
for _ in range(b):
    prod *= a

# 출력
print(prod)