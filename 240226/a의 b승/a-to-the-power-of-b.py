# 변수 선언, 입력
arr = input().split()
a = int(arr[0])
b = int(arr[1])
prod = 1

for _ in range(b):
    prod *= a

# 출력
print(prod)